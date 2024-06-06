<div align="center"><img src="assets/logo.png" width="350"></div>
<img src="assets/demo.png" >

## Preface
Link to article [YOLOX: Exceeding YOLO Series in 2021](https://paperswithcode.com/paper/yolox-exceeding-yolo-series-in-2021).


Link to original repository [YOLOX](https://github.com/Megvii-BaseDetection/YOLOX/tree/main)

## Introduction
YOLOX is an anchor-free version of YOLO, with a simpler design but better performance! It aims to bridge the gap between research and industrial communities.
For more details, please refer to our [report on Arxiv](https://arxiv.org/abs/2107.08430).

This repo is an implementation of PyTorch version YOLOX and docker version. 

<img src="assets/git_fig.png" width="1000" >

## Instructions 
1. Clone repository
```shell script
  git clone https://github.com/
```
2. Build Docker image with `docker build -t dl_project .` This process takes roughly 15-25 minutes.
3. Run the container with `docker run -p 7860:7860 -it dl_project`
4. After the container is started, open either `127.0.0.1:7860`, `0.0.0.0:7860` or `localhost:7860` in your browser. You should see the app interface.
5. To run the test, scroll to the bottom of the page and press on the first example image, then press "Detect Objects". When the output image is generated, press "Copy image to testing folder" and then "Test generated image". MSE should be around zero, while SSIM should be ~1.
6. If you want to detect objects on your own image, either drag it into the upper-left area of the app or press that area to upload your image. After that, press "Detect Objects".

https://github.com/aigc-apps/EasyAnimate/issues/27