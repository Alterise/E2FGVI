FROM pytorch/pytorch:1.11.0-cuda11.3-cudnn8-devel

WORKDIR /app

RUN apt-get update -y --allow-insecure-repositories

RUN apt install libgl1-mesa-glx -y

RUN apt-get install 'ffmpeg'\
    'libsm6'\
    'libxext6'  -y

COPY . /app

RUN conda env update --file environment.yml --prune

RUN pip install matplotlib

RUN pip install gdown

RUN gdown https://drive.google.com/uc?id=10wGdKSUOie0XmCr8SQ2A2FeDe-mfn5w3 -O release_model/

RUN pip install mmcv-full -f https://download.openmmlab.com/mmcv/dist/cu113/torch1.11.0/index.html



