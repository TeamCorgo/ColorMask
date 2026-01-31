#!/usr/bin/env bash
#set -Eeuo pipefail
#IFS=$'\n\t'

cd frontend
sudo docker stop ColorMask-frontend
sudo docker rm ColorMask-frontend
sudo docker build -t colormask-frontend .
sudo docker run -d --name ColorMask-frontend -p 9001:80 colormask-frontend