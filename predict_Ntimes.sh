#!/bin/bash
# predict N times a the same protein, take adavange of MSA precomutation
# if MSA given copy N times and send folder to predict and to where
# if not make one prediction retrieve CSV and input to YAML

N_PREDICTS="${1:-100}"
BATCH_SIZE="${2:-8}"
FILE_PREDICT="${3:? first arg: give file to predict <path.yaml>}"
TEMPERATURE="${4:-1.638}"
PRECOMPUTED_MSA="${5:-}"
WHERE_SAVE="${6:-}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG="$SCRIPT_DIR/../config.json"
get_config() { grep "\"$1\"" "$CONFIG" | sed 's/.*: *"\(.*\)".*/\1/'; }

BOLTZ=$(get_config BOLTZ_DIR)
CACHE=$(get_config BOLTZ_CACHE)
LYCAON_DIR=$(get_config LYCAON_DIR)
PROJECT_NAME="$(basename "${FILE_PREDICT%.*}")"

"$LYCAON_DIR" "$SCRIPT_DIR/titler.py" "Running ${N_PREDICTS} boltz2 prediction of ${PROJECT_NAME} " "$(date)" "" "Antonio de Palma Masaveu" "peptide"

if [[ -n "$WHERE_SAVE" ]]; then
    WORK_DIR="$WHERE_SAVE"
else
    WORK_DIR="$(cd "$(dirname "$FILE_PREDICT")" && pwd)"
fi

mkdir -p "${WORK_DIR}"
mkdir -p "${WORK_DIR}/${PROJECT_NAME}_other_files/${PROJECT_NAME}_yamls"

if [[ -n "$PRECOMPUTED_MSA" ]]; then
    cp "$PRECOMPUTED_MSA" "${WORK_DIR}/${PROJECT_NAME}_other_files/"
else
    # GPU-CPU
    if command -v nvidia-smi &>/dev/null && nvidia-smi &>/dev/null; then
        ACCELERATOR="gpu"
    else
        ACCELERATOR="cpu"
    fi

    BOLTZ_ARGS=(
        "$FILE_PREDICT"
        --use_msa_server
        --out_dir "${WORK_DIR}/${PROJECT_NAME}_other_files/"
        --cache "$CACHE"
        --use_potentials
        --recycling_steps 3
        --sampling_steps 200
        --diffusion_samples 1
        --max_parallel_samples 5
        --step_scale "$TEMPERATURE"
        --output_format mmcif
        --num_workers 12
        --preprocessing-threads 14
        --accelerator "$ACCELERATOR"
    )
    echo "No MSA provided."
    echo "Doing one run of BOLTZ2 with $PROJECT_NAME to obtain an MSA."
    BOLTZ_LOG="${WORK_DIR}/${PROJECT_NAME}_other_files/${PROJECT_NAME}_boltz2.log"
    if ! "$BOLTZ" predict "${BOLTZ_ARGS[@]}" > "$BOLTZ_LOG" 2>&1; then
        echo "Error: boltz prediction failed. See log: $BOLTZ_LOG" >&2
        exit 1
    fi
    cp "${WORK_DIR}/${PROJECT_NAME}_other_files/boltz_results_${PROJECT_NAME}/msa/${PROJECT_NAME}_0.csv" "${WORK_DIR}/${PROJECT_NAME}_other_files/"
fi

if [[ -f "${WORK_DIR}/${PROJECT_NAME}_other_files/${PROJECT_NAME}_0.csv" ]]; then
    echo ""
    echo "MSA adquired, rewritting ${PROJECT_NAME}.yaml with MSA"
fi
# ADD MSA TO YAML
ORIGINAL_BACKUP="${WORK_DIR}/${PROJECT_NAME}_other_files/$(basename "${FILE_PREDICT%.yaml}")_no_msa.yaml"
mv "$FILE_PREDICT" "$ORIGINAL_BACKUP"

echo ""
"$LYCAON_DIR" "$SCRIPT_DIR/add_MSA_to_YAML.py" \
    "$ORIGINAL_BACKUP" \
    "${WORK_DIR}/${PROJECT_NAME}_other_files/${PROJECT_NAME}_0.csv" \
    "$FILE_PREDICT"

# MAKE N_PREDICTS YAMLS
for i in $(seq -w 0 $((N_PREDICTS - 1))); do
    cp "$FILE_PREDICT" "${WORK_DIR}/${PROJECT_NAME}_other_files/${PROJECT_NAME}_yamls/${PROJECT_NAME}_${i}.yaml"
done
echo "${N_PREDICTS} yamls created at ${WORK_DIR}/${PROJECT_NAME}_other_files/${PROJECT_NAME}_yamls"
echo "Starting ${N_PREDICTS} in batches of size ${BATCH_SIZE} | expected $(((N_PREDICTS + BATCH_SIZE - 1) / BATCH_SIZE )) batches"

"$SCRIPT_DIR/boltz2_batches_mod.sh" \
    "$BATCH_SIZE" \
    "${WORK_DIR}/${PROJECT_NAME}_other_files/${PROJECT_NAME}_yamls" \
    "${WORK_DIR}/${PROJECT_NAME}_predictions" \
    "false" \
    "false" \
    "$TEMPERATURE" \
    "true"
echo ""