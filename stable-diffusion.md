## Install Stable Diffusion

### Github
```bash
https://github.com/AUTOMATIC1111/stable-diffusion-webui
```

### Install
```bash
# git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git

# Debian-based:
sudo apt install wget git python3 python3-venv libgl1 libglib2.0-0
# Red Hat-based:
sudo dnf install wget git python3 gperftools-libs libglvnd-glx 
# openSUSE-based:
sudo zypper install wget git python3 libtcmalloc4 libglvnd
# Arch-based:
sudo pacman -S wget git python3

wget -q https://raw.githubusercontent.com/AUTOMATIC1111/stable-diffusion-webui/master/webui.sh
```

### Run
```bash
# linux
python3.11 -m venv venv
source venv/bin/activate

./webui.sh --medvram --no-half-vae --xformers --share --enable-insecure-extension-access --api

# window
--xformers --lowvram --precision full --no-half --autolaunch
```

###
```bash
client id: 82190643388- 9kivj61sqn9gbbk5gv5t 41nshtb147nh.apps. googleusercontent.com
secred: GOCSPX- ya1tpak0q51J 17T8g8lxhqYtbE19
```

### Controlnet
```bash
https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/tree/main
```
