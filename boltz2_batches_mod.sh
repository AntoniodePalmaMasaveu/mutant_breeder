#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG="$SCRIPT_DIR/../config.json"
get_config() { grep "\"$1\"" "$CONFIG" | sed 's/.*: *"\(.*\)".*/\1/'; }

BOLTZ=$(get_config BOLTZ_DIR)
CACHE=$(get_config BOLTZ_CACHE)
LYCAON_DIR=$(get_config LYCAON_DIR)
BATCH_SIZE=${1:-8}
YAML_DIR=${2:-$(get_config YAMLS_DIR)}  
OUT_DIR=${3:-$(get_config PREDICTIONS_DIR)}  
USE_MSA_SERVER=${4:-true}  
MAIN=${5:-true}  
TEMPERATURE="${6:-1.638}"
SILENCED=${7:-true} 
  
mkdir -p "$OUT_DIR"

# GPU-CPU
if command -v nvidia-smi &>/dev/null && nvidia-smi &>/dev/null; then ACCELERATOR="gpu"; else ACCELERATOR="cpu"; fi

BOLTZ_ARGS=(
    --out_dir "$OUT_DIR"
    --cache "$CACHE"
    --use_potentials
    --recycling_steps 10
    --sampling_steps 200
    --diffusion_samples 1
    --max_parallel_samples 1
    --step_scale "$TEMPERATURE"
    --output_format mmcif
    --num_workers 8
    --preprocessing-threads 14
    --accelerator "$ACCELERATOR"
)
if [ "$USE_MSA_SERVER" = true ]; then
    BOLTZ_ARGS+=(--use_msa_server)
fi

INTERRUPTED=0
trap 'echo "SIGTERM received. Exiting immediately."; exit 1' TERM
trap 'echo "Interrupt received. Finishing current batch then stopping..."; INTERRUPTED=1' INT

# remove old temp file
for dir in "$OUT_DIR"/*/; do [[ "$dir" == *"boltz_batch_"* ]] && rm -rf "$dir"; done
rm -rf /tmp/boltz_batch_* 

if [ "$MAIN" = true ]; then
    "$LYCAON_DIR" "$SCRIPT_DIR/titler.py" "Running boltz2 prediction of yamls in:" "$YAML_DIR" "" "$(date)" "aminoacid"
fi

# what to do
done_names=$(ls "$OUT_DIR" | sed 's/_model_.*//' | sort -u)
needed=()
for yaml in "$YAML_DIR"/*.yaml; do
    name=$(basename "$yaml" .yaml)
    echo "$done_names" | grep -qx "$name" || needed+=("$yaml")
done

total=${#needed[@]}
echo "BOLTZ2 info: $total boltz2 predictions to run"
[ "$total" -eq 0 ] && echo "Nothing to do." && exit 0

# RUN PREDs
for (( i=0; i<total; i+=BATCH_SIZE )); do
    [ "$INTERRUPTED" -eq 1 ] && echo "Stopping after interrupt." && exit 1

    batch=("${needed[@]:$i:$BATCH_SIZE}")
    tmp="/tmp/boltz_batch_$i"
    mkdir -p "$tmp" 

    for yaml in "${batch[@]}"; do cp "$yaml" "$tmp/"; done

        if [ "$SILENCED" = true ]; then
            "$BOLTZ" predict "$tmp" "${BOLTZ_ARGS[@]}" > /dev/null 2>&1

            "$LYCAON_DIR" "$SCRIPT_DIR/progress_update.py" \
            "finished BOLTZ2 batch $((i/BATCH_SIZE+1))/$((( total+BATCH_SIZE-1)/BATCH_SIZE)) | $(date)" \
            "$((i/BATCH_SIZE + 1))" \
            "$(((total+BATCH_SIZE-1)/BATCH_SIZE))" \
            "False" #"$([ $total -gt 40 ] && echo False || echo True)"
        else
            echo ""
            echo "── Batch $((i/BATCH_SIZE+1))/$((total/BATCH_SIZE)) (${#batch[@]} structures) ──"
            date
            echo ""
            "$BOLTZ" predict "$tmp" "${BOLTZ_ARGS[@]}"
        fi

    rsync -a "$OUT_DIR/boltz_results_boltz_batch_$i/predictions/" "$OUT_DIR/"
    rm -rf "$OUT_DIR/boltz_results_boltz_batch_$i" "$tmp"
done

echo ""
echo "All predictions from $YAML_DIR finished."