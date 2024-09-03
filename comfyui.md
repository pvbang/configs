### Install
```bash
# github
git clone https://github.com/comfyanonymous/ComfyUI.git

cd ComfyUI
python3.10 -m venv venv
source venv/bin/activate

# AMD GPUs (Linux only)
# pip3.11 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm5.7
pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/rocm6.0

# NVIDIA
# pip3.11 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu121
pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu121

### fix "Torch not compiled with CUDA enabled" error
# pip uninstall torch     # and reinstall

# 
pip install -r requirements.txt

# use
python main.py --port 7766 --listen

# use gpu 0
python main.py --port 7766 --listen --cuda-device 0
```

### ComfyUI Manager
```bash
https://github.com/ltdrdata/ComfyUI-Manager

# install
python3.10 -m venv venv
source venv/bin/activate

cd ComfyUI/custom_nodes
git clone https://github.com/ltdrdata/ComfyUI-Manager
cd ..
python -m pip install -r custom_nodes/ComfyUI-Manager/requirements.txt
```


### Config models path
```bash
mkdir saves
cd saves
mkdir checkpoints clip clip_vision configs controlnet embeddings loras upscale_models vae
cd checkpoints
mkdir SD1.5 SDXL Inpainting SVD

echo "comfyui:
    checkpoints: /home/ubuntu/pvbang/saves/checkpoints/
    clip: /home/ubuntu/pvbang/saves/clip/
    clip_vision: /home/ubuntu/pvbang/saves/clip_vision/
    configs: /home/ubuntu/pvbang/saves/configs/
    controlnet: /home/ubuntu/pvbang/saves/controlnet/
    embeddings: /home/ubuntu/pvbang/saves/embeddings/
    loras: /home/ubuntu/pvbang/saves/loras/
    upscale_models: /home/ubuntu/pvbang/saves/upscale_models/
    vae: /home/ubuntu/pvbang/saves/vae/" > extra_model_paths.yaml
```

### Clone ComfyUI
```bash
cp -r comfyui-image-generate-1 comfyui-image-generate-2
screen -S comfyui-image-generate-2
cd comfyui-image-generate-2
cd ComfyUI
source venv/bin/activate

# comfyui-image-generate-1
python main.py --port 7700 --listen --cuda-device 0

# comfyui-image-generate-2
python main.py --port 7702 --listen --cuda-device 1

# comfyui-image-generate-3
python main.py --port 7704 --listen --cuda-device 2

# comfyui-image-generate-4
python main.py --port 7706 --listen --cuda-device 3

# comfyui-image-generate-5
python main.py --port 7708 --listen --cuda-device 4

# comfyui-image-generate-6
python main.py --port 7710 --listen --cuda-device 5

# comfyui-image-generate-7
python main.py --port 7712 --listen --cuda-device 6

# comfyui-image-generate-8
# python main.py --port 7714 --listen --cuda-device 7
```