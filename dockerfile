FROM python:3.9

WORKDIR /app

COPY . /app/YOLOX

WORKDIR /app/YOLOX

RUN apt-get update && apt-get install -y \
    git \
    curl \
    g++ \
    make \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -U pip && pip install -r requirements.txt

RUN python3 setup.py develop

CMD ["python", "tools/demo.py", "image", "-n", "yolox-s", "-c", "yolox_s.pth", "--path", "dog.jpg", "--conf", "0.25", "--nms", "0.45", "--tsize", "640", "--save_result", "--device", "cpu"]
