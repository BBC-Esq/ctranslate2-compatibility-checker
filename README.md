# Check Ctranslate2 Quantization Support for CPU and GPU

### For Windows

Simply download and run the executable in the release section to check which quantizations your CPU and GPU support.

## For Linux or MacOS

Step 1 - Download [```ctranslate2_compatibility.py```](https://github.com/BBC-Esq/ctranslate2-compatibility-checker/blob/a73ca3407df552fbc0da675b4c728ee898bfaf9b/ctranslate2_compatibility.py) and [```requirements.txt```](https://github.com/BBC-Esq/ctranslate2-compatibility-checker/blob/main/requirements.txt) to a folder.

Step 2 - Within that folder, open a command prompt and create a virtual environment:
```
python -m venv
```

Step 3 - Activate Virtual Environment
```
source bin/activate
```

Step 4 - Upgrade Pip
```
python -m pip install --upgrade pip
```

Step 5 - If you have an Nvidia GPU run:
```
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

Step 6 - Install Dependencies
```
pip install -r requirements.txt
```

Step 7 - Check Compatible Quantizations
```
python ctranslate2_compatibility.py
```
