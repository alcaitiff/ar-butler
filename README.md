# AR-Butler

![Logo](./assets/logo.png)

This is an python application to listen your commands and answer your questions using local LLMs and RAG.

## Installation

To install you will need to clone the repository and download the dependecies.
Normally I use conda to separate python environments.

```bash
git clone https://github.com/alcaitiff/ar-butler.git
cd ar-butler
conda create -n ar-butler python=3.10
conda activate ar-butler
conda install pytorch==2.0.0 torchaudio==2.0.0 torchvision pytorch-cuda=11.8 -c pytorch -c nvidia && pip install git+https://github.com/m-bain/whisperx.git
pip install -r requirements.txt
```

## Usage

```bash
python3 app.py
```
