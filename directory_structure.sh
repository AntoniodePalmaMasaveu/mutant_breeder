#!/bin/bash

echo "        H      R      H        "
echo "   +    |      |      |    -   "
echo "    H3N-C-CONH-C-CONH-C-COO    "
echo "        |      |      |        "
echo "        R      H      R        "

echo ""
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG="$SCRIPT_DIR/files_utilities/config.json"
get_config() { grep "\"$1\"" "$CONFIG" | sed 's/.*: *"\(.*\)".*/\1/'; }

if [ -f "$CONFIG" ] && [ "$(get_config setup_done)" = "done" ]; then
    echo "Setup already done. Not repeating it."
    exit 0
fi

echo "Setting directories and enviroments:"

mkdir -p protein_files/yamls
mkdir -p protein_files/boltz2_predictions
mkdir -p protein_files/rosetta_relaxed

mkdir -p files_utilities/boltz2_cache
mkdir -p files_utilities/antonios

# tracking fails
FAILED=""
CONDA_DIR="$(pwd)/files_utilities/conda"

curl -L https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh -o /tmp/miniforge.sh
bash /tmp/miniforge.sh -b -p "$CONDA_DIR"
rm /tmp/miniforge.sh
source "$CONDA_DIR/etc/profile.d/conda.sh" || FAILED="conda setup"


conda create -p "$CONDA_DIR/envs/boltz2" python=3.12 -y
conda run -p "$CONDA_DIR/envs/boltz2" pip install --upgrade pip
conda run -p "$CONDA_DIR/envs/boltz2" pip install boltz ipykernel #cuequivariance-torch 
conda run -p "$CONDA_DIR/envs/boltz2" python -m ipykernel install --user --name boltz2 --display-name "boltz2" || FAILED="boltz2 setup"

conda create -p "$CONDA_DIR/envs/rosetta" python=3.12 -y
conda run -p "$CONDA_DIR/envs/rosetta" pip install --upgrade pip
conda run -p "$CONDA_DIR/envs/rosetta" pip install pyrosetta ipykernel \
    --find-links https://west.rosettacommons.org/pyrosetta/quarterly/minsizerel
conda run -p "$CONDA_DIR/envs/rosetta" python -m ipykernel install --user --name rosetta --display-name "rosetta" || FAILED="rosetta setup"

conda create -p "$CONDA_DIR/envs/lycaon" python=3.12 -y
conda run -p "$CONDA_DIR/envs/lycaon" pip install --upgrade pip
conda run -p "$CONDA_DIR/envs/lycaon" pip install numpy pandas matplotlib seaborn scipy gemmi ipykernel
conda run -p "$CONDA_DIR/envs/lycaon" pip install pyyaml
conda run -p "$CONDA_DIR/envs/lycaon" python -m ipykernel install --user --name lycaon --display-name "lycaon" || FAILED="lycaon setup"

conda config --append envs_dirs "$CONDA_DIR/envs"

#its pyrosetta Y should change the name
MOTHER="$(pwd)"
BOLTZ2_CACHE=$(find $HOME -name "boltz2_aff.ckpt" -o -name "boltz2_conf.ckpt" 2>/dev/null | head -1 | xargs dirname 2>/dev/null)
if [ -n "$BOLTZ2_CACHE" ]; then
    echo "Boltz2 cache found at: $BOLTZ2_CACHE, going to use it to avoid redowload of models"
else
    BOLTZ2_CACHE="$MOTHER/files_utilities/boltz2_cache"
    echo "Boltz2 cache not found, on first prediction needed files will be installed at: $BOLTZ2_CACHE"
fi

cat > files_utilities/config.json << EOF
{
    "MOTHER_DIR":      "$MOTHER",
    "WORKING_DIR":     "$MOTHER/files_utilities",
    "YAMLS_DIR":       "$MOTHER/protein_files/yamls",
    "PREDICTIONS_DIR": "$MOTHER/protein_files/boltz2_predictions",
    "RELAXED_DIR":     "$MOTHER/protein_files/rosetta_relaxed",
    "BOLTZ_DIR":       "$MOTHER/files_utilities/conda/envs/boltz2/bin/boltz",
    "BOLTZ_CACHE":     "$BOLTZ2_CACHE",
    "LYCAON_DIR":      "$MOTHER/files_utilities/conda/envs/lycaon/bin/python",
    "ROSETTA_DIR":     "$MOTHER/files_utilities/conda/envs/rosetta/bin/python",
    "ANTONIOS_DIR":    "$MOTHER/files_utilities/antonios"
    "setup_done":      "done"
}
EOF

if [ -n "$FAILED" ]; then
    echo ""
    echo "Setup failed at: $FAILED"
    echo "deleting..."
    rm -rf files_utilities
    exit 1
fi

echo ""
echo "All done! Activate environments with:"
echo "conda activate ./files_utilities/conda/envs/boltz2"
echo "conda activate ./files_utilities/conda/envs/rosetta"
echo "conda activate ./files_utilities/conda/envs/lycaon"
echo ""
./tree.sh

# RuntimeError: Failed to find C compiler. Please specify via CC environment variable or set triton.knobs.build.impl.
#sudo apt update && sudo apt install gcc -y