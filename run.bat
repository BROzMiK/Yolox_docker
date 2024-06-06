@echo off
REM Get the current directory
set CURRENT_DIR=%cd%

REM Run the Docker container with volume mapping
docker run --rm -v %CURRENT_DIR%\outputs:/app/YOLOX/YOLOX_outputs yolox-demo
