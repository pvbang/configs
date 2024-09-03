## Install Facefusion in Linux

### Document
```bash
https://docs.facefusion.io/installation
```

### Install
```bash
rm -r facefusion

git clone https://github.com/facefusion/facefusion

cd facefusion

python3.11 -m venv venv
source venv/bin/activate

python install.py

python run.py

# fix FFMpeg is not installed
sudo apt install ffmpeg
```


