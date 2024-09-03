### Install Kohya_ss in Linux

## Install CUDA
```bash
# instruction
https://www.cherryservers.com/blog/install-cuda-ubuntu

# website
https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=22.04&target_type=deb_network

# install
wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-keyring_1.1-1_all.deb
sudo dpkg -i cuda-keyring_1.1-1_all.deb
sudo apt-get update
sudo apt-get -y install cuda-toolkit-12-3
```

## Setup
```bash
git clone https://github.com/bmaltais/kohya_ss.git 
cd kohya_ss

python3.10 -m venv venv
source venv/bin/activate 

pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/rocm5.6
pip install --use-pep517 --upgrade -r requirements.txt

accelerate config
- This machine
- No distributed training
- no
- no
- no
- all
- fp16

sudo apt-get install python3-tk
export HSA_OVERRIDE_GFX_VERSION=10.3.0
source venv/bin/activate
python kohya_gui.py "$@"

# fix
pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116
export DISPLAY=:0.0
echo $DISPLAY
sudo reboot now

# docker
git clone https://github.com/bmaltais/kohya_ss.git
cd kohya_ss
docker compose create
docker compose build
docker compose run --service-ports kohya-ss-gui

sudo apt-get install x11-apps
export DISPLAY=:0

# sd
curl --output anaconda.sh https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Linux-x86_64.sh
sha256sum anaconda.sh
bash anaconda.sh
source ~/.bashrc
```
