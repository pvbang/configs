### Cài Python3.11 nếu chưa có
```sh
sudo apt update
sudo apt install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget

wget https://www.python.org/ftp/python/3.11.7/Python-3.11.7.tgz
tar -xvf Python-3.11.7.tgz
cd Python-3.11.7
./configure --enable-optimizations
sudo make altinstall
python3.11 --version
sudo ln -sf /usr/local/bin/python3.11 /usr/bin/python
```


### Config
```sh
sudo su
mkdir mekongai
cd mekongai

git clone https://github.com/ostris/ai-toolkit.git
cd ai-toolkit
git submodule update --init --recursive

python3.11 -m venv venv
source venv/bin/activate

pip3.11 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu121
pip3.11 install -r requirements.txt
```

### Run
```sh
python3.11 run.py /home/ubuntu/mekongai/ai-toolkit/config/train_lora_flux_24gb_tonghop.yaml
```


### Fix lỗi: RuntimeError: view size is not compatible with input tensor's size and stride (at least one dimension spans across two contiguous subspaces). Use .reshape(...) instead.
```sh
nano /home/ubuntu/mekongai/ai-toolkit/venv/lib/python3.11/site-packages/optimum/quanto/tensor/weights/qbytes.py

# Kéo xuống tí
# Sửa:
output = torch.ops.quanto.qbytes_mm(input.view(-1, in_features), other

# Thành: 
output = torch.ops.quanto.qbytes_mm(input.reshape(-1, in_features), other
```


### Fix lỗi: Nvidia
```sh
sudo apt-get update
sudo apt-get install -y nvidia-cuda-toolkit

sudo apt-get update
sudo apt-get install -y cuda-12-2

sudo ln -s /usr/local/cuda-12.2 /usr/local/cuda
export CUDA_HOME=/usr/local/cuda
export PATH=$CUDA_HOME/bin:$PATH
export LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH
```


libGL.so.1: cannot open shared object file
sudo apt update
sudo apt install -y libgl1-mesa-glx libglib2.0-0


### train_lora_flux_24gb_tonghop.yaml
```sh
job: extension
config:
  name: "lora_noel"
  process:
    - type: 'sd_trainer'
      training_folder: "output"
      device: cuda:0
      trigger_word: "box"
      network:
        type: "lora"
        linear: 64
        linear_alpha: 64
      save:
        dtype: float16
        save_every: 250
        max_step_saves_to_keep: 12
        push_to_hub: false
      datasets:
        - folder_path: "/home/ubuntu/train/noel"
          caption_ext: "txt"
          caption_dropout_rate: 0.05
          shuffle_tokens: false
          cache_latents_to_disk: true
          resolution: [ 512, 768,1024  ]  # flux enjoys multiple resolutions
      train:
        batch_size: 4
        steps: 20000
        gradient_accumulation_steps: 2  # Increased to reduce memory per step
        train_unet: true
        train_text_encoder: false
        gradient_checkpointing: true
        noise_scheduler: "flowmatch"
        optimizer: "adamw8bit"
        lr: 5e-5
        ema_config:
          use_ema: true
          ema_decay: 0.99
        dtype: bf16
      model:
        name_or_path: "black-forest-labs/FLUX.1-dev"
        is_flux: true
        quantize: true
        low_vram: true  # Enabled low VRAM mode to reduce memory usage
      sample:
        sampler: "flowmatch"
        sample_every: 250
        width: 1024  
        height: 1024  
        prompts:
          - "vunguyet, The woman is wearing a light white off-shoulder shirt. The shirt is designed to hug the body, with elastic material to help accentuate the body's curves and create a feeling of comfort. The off-shoulder neckline reveals the bare shoulders, creating a feminine and seductive beauty. Off-shoulder design"
          - "vunguyet, The woman is wearing a light white off-shoulder shirt. The shirt is designed to hug the body, with elastic material to help accentuate the body's curves and create a feeling of comfort. The off-shoulder neckline reveals the bare shoulders, creating a feminine and seductive beauty. Off-shoulder design"
          - "vunguyet, The woman is wearing a light white off-shoulder shirt. The shirt is designed to hug the body, with elastic material to help accentuate the body's curves and create a feeling of comfort. The off-shoulder neckline reveals the bare shoulders, creating a feminine and seductive beauty. Off-shoulder design"
          - "vunguyet, The woman is wearing a light white off-shoulder shirt. The shirt is designed to hug the body, with elastic material to help accentuate the body's curves and create a feeling of comfort. The off-shoulder neckline reveals the bare shoulders, creating a feminine and seductive beauty. Off-shoulder design"
        neg: ""
        seed: 42
        walk_seed: true
        guidance_scale: 4
        sample_steps: 20
meta:
  name: "[name]"
  version: '1.0'
```