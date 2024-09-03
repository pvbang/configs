### Gihub
```bash
https://github.com/lllyasviel/Fooocus
```

### Install (Windows)
```bash
# download
https://github.com/lllyasviel/Fooocus/releases/download/release/Fooocus_win64_2-1-831.7z

# run
run.bat

# anime
run_anime.bat

# realistic
run_realistic.bat
```

### Install (Linux)
```bash
# python 3.10
git clone https://github.com/lllyasviel/Fooocus.git
cd Fooocus
python3.10 -m venv fooocus_env
source fooocus_env/bin/activate
pip install -r requirements_versions.txt

source fooocus_env/bin/activate

# run
python entry_with_update.py --listen

# anime
python entry_with_update.py --preset anime

# realistic
python entry_with_update.py --preset realistic
```