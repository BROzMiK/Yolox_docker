<div align="center"><img src="assets/logo.png" width="350"></div>
<img src="assets/demo.png" >

## Preface
Link to article [YOLOX: Exceeding YOLO Series in 2021](https://paperswithcode.com/paper/yolox-exceeding-yolo-series-in-2021).


Link to original repository [YOLOX](https://github.com/Megvii-BaseDetection/YOLOX/tree/main)

## Introduction
YOLOX is an anchor-free version of YOLO, with a simpler design but better performance! It aims to bridge the gap between research and industrial communities.
For more details, please refer to [report on Arxiv](https://arxiv.org/abs/2107.08430).

This repo is an implementation of PyTorch version YOLOX and docker version of YOLOX. 

<img src="assets/git_fig.png" width="1000" >

## Instructions 
1. Clone repository
```shell script
  git clone https://github.com/BROzMiK/Yolox_docker.git
```
2. Download and put this model in the root folder :
|[YOLOX-s](./exps/default/yolox_s.py)    |640  |40.5 |40.5      |9.8      |9.0 | 26.8 | [github](https://github.com/Megvii-BaseDetection/YOLOX/releases/download/0.1.1rc0/yolox_s.pth) |
3. Launch Docker Desktop
4. Run `build.bat` and wait about 10-20 min
5. Run `run.bat` for default parameters
6. Check the result in "outputs" folder

## Test
1. Put image from "outputs" folder in the root folder.
2. Run 'compare_detections.py'
