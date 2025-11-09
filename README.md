# Fanfiction-20251111

2025 爱莉希雅 生贺

## OCR Env

CPU:

```shell
conda create -y -n ely python=3.11
conda activate ely
conda install pytorch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 numpy pillow==9.4.0 easyocr cpuonly -c pytorch -y
conda install keyboard -c conda-forge
```

GPU:

```shell
conda create -y -n ely python=3.11
conda activate ely
conda install pytorch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 numpy pillow==9.4.0 easyocr ninja opencv pytorch-cuda=12.1 -c pytorch -c nvidia
conda install keyboard pyperclip -c conda-forge
pip install opencv-contrib-python==4.11.0.86 --dry-run
pip install opencv-contrib-python==4.11.0.86
```

## CnOCR Env

GPU:

```shell
conda create -y -n cnocr313 python=3.13
conda activate cnocr313
pip install torch==2.7.1 torchvision==0.22.1 torchaudio==2.7.1 numpy==2.2.6 pillow --index-url https://download.pytorch.org/whl/cu128 --dry-run
pip install cnocr[ort-gpu] --dry-run
conda install keyboard pyperclip -c conda-forge
```
