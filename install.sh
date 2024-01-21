#/bin/bash

root_dir=$(pwd)
echo "Setting up the environment in the $root_dir"

echo "Creating a virtual environment with python3"
conda create -n hf2 python -y
conda activate hf2

echo "Installing all the dependencies"

pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu121
pip install sentencepiece deepspeed datasets packaging

MAX_JOBS=4 pip install flash-attn --no-build-isolation
conda install mpi4py -y
pip install git+https://github.com/abhinand5/transformers.git@abhinand5-deepspeed-patch
pip install git+https://github.com/huggingface/peft.git@13e53fc

echo "Setup completed!"