```bash
############################################################################################################ 
### Remote Desktop
sudo apt update
sudo apt install ubuntu-desktop -y
sudo apt install xrdp -y
sudo adduser xrdp ssl-cert

sudo systemctl restart xrdp
sudo passwd ubuntu


############################################################################################################
### rclone setup
cd /root/
wget https://downloads.rclone.org/rclone-current-linux-amd64.zip
unzip rclone-current-linux-amd64.zip
sudo cp rclone-v*-linux-amd64/rclone /usr/sbin/
rm -rf rclone-*

rclone config
n
mekongai
17
703033512826- ...
GOCSPX-6s ...
1
n
n

# screen 
cd mekongai
rclone sync mekongai:ComfyUI/comfyui-image-generate-1.zip comfyui-image-generate-1.zip
rclone sync mekongai:ComfyUI/comfyui-face-swap-1.zip comfyui-face-swap-1.zip
rclone sync mekongai:ComfyUI/comfyui-ootdiffusion-1.zip comfyui-ootdiffusion-1.zip
rclone sync mekongai:ComfyUI/saves saves

unzip comfyui-image-generate-1.zip/comfyui-image-generate-1.zip
unzip comfyui-face-swap-1.zip/comfyui-face-swap-1.zip
unzip comfyui-ootdiffusion-1.zip/comfyui-ootdiffusion-1.zip

cd saves
unzip checkpoints.zip
unzip embeddings.zip
unzip loras.zip
unzip vae.zip
unzip instantid.zip
unzip clip_vision.zip
unzip upscale_models.zip
unzip inpaint.zip
unzip ipadapter.zip
unzip insightface.zip

############################################################################################################
### Cloudflare: https://one.dash.cloudflare.com/195f5955360a5210b2802446fc2de018/networks/tunnels/cfd_tunnel/2292a62f-ac46-4fd8-a269-8395e7a16a44/edit?tab=overview
curl -L --output cloudflared.deb https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb && 
sudo dpkg -i cloudflared.deb && 
sudo cloudflared service install eyJhIjoiMTk1ZjU5NTUzN...

# And Config Public host names Cloudflare


############################################################################################################
### Install Nvidia
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt install ubuntu-drivers-common
sudo ubuntu-drivers devices
sudo ubuntu-drivers autoinstall
sudo reboot


### Gỡ Nvidia cài lại
sudo apt-get remove --purge '^nvidia-.*'
sudo apt-get autoremove
sudo apt-get autoclean
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt-get update
sudo apt-get install nvidia-driver-535
sudo reboot


# Open VPS and Download models, folder ComfyUI,...


############################################################################################################
### Fix lỗi khi sudo apt update
sudo apt install --reinstall python3-minimal dh-python

sudo apt-get clean
sudo apt-get update
sudo apt-get upgrade

nano /home/ubuntu/mekongai/ai-toolkit/venv/lib/python3.11/site-packages/optimum/quanto/tensor/weights/qbytes.py
sửa output = torch.ops.quanto.qbytes_mm(input.view(-1, in_features), other
thành output = torch.ops.quanto.qbytes_mm(input.reshape(-1, in_features), other

python3.11 run.py /home/ubuntu/mekongai/ai-toolkit/config/train_lora_flux_24gb_tonghop.yaml


############################################################################################################
### 3.11.9
sudo apt update
sudo apt install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
wget https://www.python.org/ftp/python/3.11.7/Python-3.11.7.tgz
tar -xvf Python-3.11.7.tgz
cd Python-3.11.7
./configure --enable-optimizations
sudo make altinstall
python3.11 --version
sudo ln -sf /usr/local/bin/python3.11 /usr/bin/python


############################################################################################################
### Config models path
mkdir mekongai
cd mekongai
mkdir saves
cd mekongai/saves
mkdir checkpoints clip clip_vision configs controlnet embeddings loras upscale_models vae inpaint ipadapter insightface
cd mekongai/saves/checkpoints
mkdir SD1.5 SDXL Inpainting SVD
cd mekongai/saves/controlnet
mkdir instantid
cd mekongai/saves/insightface
mkdir models
cd mekongai/saves/insightface/models
mkdir antelopev2

echo "comfyui:
    checkpoints: /home/ubuntu/mekongai/saves/checkpoints/
    clip: /home/ubuntu/mekongai/saves/clip/
    clip_vision: /home/ubuntu/mekongai/saves/clip_vision/
    configs: /home/ubuntu/mekongai/saves/configs/
    controlnet: /home/ubuntu/mekongai/saves/controlnet/
    embeddings: /home/ubuntu/mekongai/saves/embeddings/
    loras: /home/ubuntu/mekongai/saves/loras/
    upscale_models: /home/ubuntu/mekongai/saves/upscale_models/
    vae: /home/ubuntu/mekongai/saves/vae/
    inpaint: /home/ubuntu/mekongai/saves/inpaint/
    instantid: /home/ubuntu/mekongai/saves/controlnet/instantid/
    insightface: /home/ubuntu/mekongai/saves/insightface/
    antelopev2: /home/ubuntu/mekongai/saves/insightface/models/antelopev2/
    facerestore_models: /home/ubuntu/mekongai/saves/facerestore_models/" > extra_model_paths.yaml


############################################################################################################
### SSL cho API
mkdir ssl
cd mekongai/ssl/

# Tạo khóa riêng (private key)
openssl genpkey -algorithm RSA -out server.key -pkeyopt rsa_keygen_bits:2048

# Tạo chứng chỉ tự ký (self-signed certificate)
openssl req -new -x509 -key server.key -out server.crt -days 365


############################################################################################################
### API 
# API MekongAI
screen -S api-mekongai
cd mekongai/mekongai-comfyui
python3.11 -m venv venv
source venv/bin/activate
pip3.11 install -r requirements.txt
python3.11 app_mekongai.py

# API Public
screen -S api-public
cd mekongai/mekongai-comfyui
source venv/bin/activate
python3.11 app_public.py

# API Image
screen -S api-images
cd mekongai/mekongai-comfyui
source venv/bin/activate
python3.11 app_images.py

# API website
screen -S python-api-mekongai-ai-images
cd mekongai/python-api-mekongai-ai-images
python3.11 -m venv venv
source venv/bin/activate
pip3.11 install -r requirements.txt
python3.11 app.py

# API chatbot
screen -S mekongai-chatbots
cd mekongai/mekongai-chatbots
python3.11 -m venv venv
source venv/bin/activate
pip3.11 install -r requirements.txt
python3.11 app.py


############################################################################################################
screen -S saves
mkdir mekongai/saves
aws s3 cp s3://mekongai/saves mekongai/saves --recursive --profile MAIN


############################################################################################################
### Clone ComfyUI Image Generate
# comfyui-image-generate-1
screen -S comfyui-image-generate-1
mkdir mekongai/comfyui-image-generate-1
aws s3 cp s3://mekongai/comfyui-image-generate-1 mekongai/comfyui-image-generate-1 --recursive --profile MAIN
cd mekongai/comfyui-image-generate-1/ComfyUI
source venv/bin/activate
python3.11 main.py --port 7700 --listen --cuda-device 0

# comfyui-image-generate-2
screen -S comfyui-image-generate-2
mkdir mekongai/comfyui-image-generate-2
aws s3 cp s3://mekongai/comfyui-image-generate-2 mekongai/comfyui-image-generate-2 --recursive --profile MAIN
cd mekongai/comfyui-image-generate-2/ComfyUI
source venv/bin/activate
python3.11 main.py --port 7702 --listen --cuda-device 1

# comfyui-image-generate-3
screen -S comfyui-image-generate-3
mkdir mekongai/comfyui-image-generate-3
aws s3 cp s3://mekongai/comfyui-image-generate-3 mekongai/comfyui-image-generate-3 --recursive --profile MAIN
cd mekongai/comfyui-image-generate-3/ComfyUI
source venv/bin/activate
python3.11 main.py --port 7704 --listen --cuda-device 2

# comfyui-image-generate-4
cp -r comfyui-image-generate-1 comfyui-image-generate-4
screen -S comfyui-image-generate-4
cd mekongai/comfyui-image-generate-4/ComfyUI
source venv/bin/activate
python3.11 main.py --port 7706 --listen --cuda-device 3

# comfyui-image-generate-5
cp -r comfyui-image-generate-1 comfyui-image-generate-5
screen -S comfyui-image-generate-5
cd mekongai/comfyui-image-generate-5/ComfyUI
source venv/bin/activate
python3.11 main.py --port 7708 --listen --cuda-device 4

# comfyui-image-generate-6
cp -r comfyui-image-generate-1 comfyui-image-generate-6
screen -S comfyui-image-generate-6
cd mekongai/comfyui-image-generate-6/ComfyUI
source venv/bin/activate
python3.11 main.py --port 7710 --listen --cuda-device 5

# comfyui-image-generate-7
cp -r comfyui-image-generate-1 comfyui-image-generate-7
screen -S comfyui-image-generate-7
cd mekongai/comfyui-image-generate-7/ComfyUI
source venv/bin/activate
python3.11 main.py --port 7712 --listen --cuda-device 6

# comfyui-image-generate-8
screen -S comfyui-image-generate-8
mkdir mekongai/comfyui-image-generate-8
aws s3 cp s3://mekongai/comfyui-image-generate-8 mekongai/comfyui-image-generate-8 --recursive --profile MAIN
cd mekongai/comfyui-image-generate-8/ComfyUI
source venv/bin/activate
python3.11 main.py --port 7714 --listen --cuda-device 7



### ComfyUI Image Face Swap
screen -S comfyui-face-swap-1
cd mekongai/comfyui-face-swap-1/ComfyUI
source venv/bin/activate
pip3.11 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu121
pip3.11 install -r requirements.txt
python3.11 main.py --port 7800 --listen --cuda-device 1

### ComfyUI Image Outfit Swap
screen -S comfyui-ootdiffusion-1
mkdir mekongai/comfyui-ootdiffusion-1
aws s3 cp s3://mekongai/comfyui-ootdiffusion-1 mekongai/comfyui-ootdiffusion-1 --recursive --profile MAIN
cd mekongai/comfyui-ootdiffusion-1/ComfyUI
source venv/bin/activate
pip3.11 install -r requirements.txt
pip3.11 install -r custom_nodes/ComfyUI-OOTDiffusion/requirements.txt
python3.11 main.py --port 7900 --listen --cuda-device 2

### ComfyUI Image Children
screen -S comfyui-child
cd cd mekongai/comfyui-child/ComfyUI
source venv/bin/activate
pip install -r requirements.txt
python3.10 main.py --port 8000 --listen --cuda-device 3

### ComfyUI Image Nude
screen -S comfyui-image-nude
cd mekongai/comfyui-image-nude/ComfyUI
source venv/bin/activate
python3.10 main.py --port 7600 --listen --cuda-device 4


############################################################################################################
###
sudo apt update
sudo apt install git-lfs

cd mekongai/saves/controlnet
git lfs install
git clone https://huggingface.co/lllyasviel/ControlNet-v1-1
git clone https://huggingface.co/ckpt/controlnet-sdxl-1.0

cd mekongai/saves/controlnet/instantid
wget -O diffusion_pytorch_model.safetensors https://huggingface.co/InstantX/InstantID/resolve/main/ControlNetModel/diffusion_pytorch_model.safetensors?download=true

cd mekongai/saves/ipadapter
git lfs install
git clone https://huggingface.co/h94/IP-Adapter

cd mekongai/saves/instantid 
wget -O ip-adapter.bin https://huggingface.co/InstantX/InstantID/resolve/main/ip-adapter.bin?download=true

cd mekongai/saves/insightface/models/antelopev2
wget -O antelopev2.zip https://drive.google.com/file/d/18wEUfMNohBJ4K3Ly5wpTejPfDzp-8fI8/view?usp=sharing
```


### Backup
```bash
# upload s3
export AWS_ACCESS_KEY_ID= 
export AWS_SECRET_ACCESS_KEY=

aws s3 ls s3://

# aws s3 cp comfyui-image-generate-8.zip s3://comfyui-image-generate
# aws s3 cp s3://comfyui-image-generate/comfyui-image-generate-8.zip .

export AWS_ACCESS_KEY_ID=A
export AWS_SECRET_ACCESS_KEY=
mkdir mekongai
mkdir mekongai/saves
cd mekongai/saves 
aws s3 cp checkpoints.zip s3://bucket-comfyui/saves/checkpoints.zip
aws s3 cp clip_vision.zip s3://bucket-comfyui/saves/clip_vision.zip
aws s3 cp instantid.zip s3://bucket-comfyui/saves/instantid.zip
aws s3 cp upscale_models.zip s3://bucket-comfyui/saves/upscale_models.zip
aws s3 cp inpaint.zip s3://bucket-comfyui/saves/inpaint.zip
aws s3 cp loras.zip s3://bucket-comfyui/saves/loras.zip
aws s3 cp embeddings.zip s3://bucket-comfyui/saves/embeddings.zip
aws s3 cp ipadapter.zip s3://bucket-comfyui/saves/ipadapter.zip
aws s3 cp vae.zip s3://bucket-comfyui/saves/vae.zip

### dowload
aws s3 cp s3://bucket-comfyui/saves/clip_vision.zip .
aws s3 cp s3://bucket-comfyui/saves/instantid.zip .
aws s3 cp s3://bucket-comfyui/saves/upscale_models.zip .
aws s3 cp s3://bucket-comfyui/saves/inpaint.zip .
aws s3 cp s3://bucket-comfyui/saves/loras.zip .
aws s3 cp s3://bucket-comfyui/saves/embeddings.zip .
aws s3 cp s3://bucket-comfyui/saves/ipadapter.zip .
aws s3 cp s3://bucket-comfyui/saves/vae.zip .
aws s3 cp s3://bucket-comfyui/saves/checkpoints.zip .

aws s3 cp s3://bucket-comfyui/comfyui-image-generate-8.zip .
aws s3 cp s3://bucket-comfyui/comfyui-face-swap-1.zip .
aws s3 cp s3://bucket-comfyui/comfyui-ootdiffusion-1.zip .

cd mekongai
export AWS_ACCESS_KEY_ID=
export AWS_SECRET_ACCESS_KEY=
aws s3 cp comfyui-image-generate-8.zip s3://bucket-comfyui/comfyui-image-generate-8.zip
aws s3 cp comfyui-face-swap-1.zip s3://bucket-comfyui/comfyui-face-swap-1.zip
aws s3 cp comfyui-ootdiffusion-1.zip s3://bucket-comfyui/comfyui-ootdiffusion-1.zip

# backup mekongai
aws s3 cp /mekongai s3://mekongai --recursive

# xóa thùng rác
rm -rf ~/.local/share/Trash/*

# upload lên s3
aws s3 cp mekongai s3://mekongai/ --recursive --profile MAIN
aws s3 cp mekongai s3://playpikk/ --recursive --profile AUGFY
aws s3 cp mekongai s3://new-bucket-2fda1afe/ --recursive --profile HNLSRQ
aws s3 cp mekongai s3://cdn.leadiffer.cn/tests/ --recursive

# update thay đổi lên s3
aws s3 sync mekongai s3://mekongai/ --exact-timestamps --profile MAIN
aws s3 sync mekongai s3://playpikk/ --exact-timestamps --profile AUGFY
aws s3 sync mekongai s3://new-bucket-2fda1afe/ --exact-timestamps --profile HNLSRQ
aws s3 sync mekongai s3://cdn.leadiffer.cn/tests/ --exact-timestamps

# yolo_train
aws s3 sync yolo_train s3://mekongai/dung/yolo_train --exact-timestamps --profile MAIN
aws s3 sync yolo_train s3://mekongai/dung/yolo_train --exact-timestamps --profile AUGFY
aws s3 sync yolo_train s3://mekongai/dung/yolo_train --exact-timestamps --profile HNLSRQ
aws s3 sync yolo_train s3://mekongai/dung/yolo_train --exact-timestamps --profile MAIN

# Xem ls s3
aws s3 ls --profile MAIN
aws s3 ls s3://playpikk --profile AUGFY
aws s3 ls s3://new-bucket-2fda1afe --profile HNLSRQ
aws s3 ls s3://cdn.leadiffer.cn/tests

# Download về
aws s3 cp s3://mekongai/ mekongai/ --recursive --profile MAIN

mkdir mekongai
mkdir mekongai/comfyui-image-generate-8
aws s3 cp s3://mekongai/comfyui-image-generate-8 mekongai/comfyui-image-generate-8 --recursive --profile MAIN
mkdir mekongai/saves
aws s3 cp s3://mekongai/saves mekongai/saves --recursive --profile MAIN

```


### API
```bash
git clone https://github.com/pvbang/mekongai-chatbots.git

git clone https://github.com/pvbang/python-api-mekongai-ai-images.git
```

### Fix No space left on device khi df -h vẫn còn
```sh
sudo rm -rf /tmp/*
pip cache purge
sudo mount -o remount,size=10G /tmp
```