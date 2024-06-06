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
2. Launch Docker Desktop
3. Run `build.bat` and wait about 10-20 min
4. Run `run.bat` for default parameters
5. Check the result in "outputs" folder

## Test
1. Put image from "outputs" folder in the root folder.
2. Run 'compare_detections.py'
