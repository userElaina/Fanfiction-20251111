# Fanfiction-20251111

2025 爱莉希雅 生贺

## Env

CPU:

```sh
conda create -y -n ely python=3.11
conda activate ely
conda install pytorch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 numpy pillow==9.4.0 easyocr cpuonly -c pytorch -y
conda install keyboard -c conda-forge
```

GPU:

```sh
conda create -y -n ely python=3.11
conda activate ely
conda install pytorch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 numpy pillow==9.4.0 easyocr ninja opencv pytorch-cuda=12.1 -c pytorch -c nvidia
conda install keyboard -c conda-forge
pip install opencv-contrib-python==4.11.0.86 --dry-run
pip install opencv-contrib-python==4.11.0.86
```
