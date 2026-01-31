#!/usr/bin/env bash
#set -Eeuo pipefail
#IFS=$'\n\t'

cd backend
sudo docker stop ColorMask-backend
sudo docker rm ColorMask-backend
sudo docker build -t colormask-backend .
sudo docker run -d --name ColorMask-backend -p 9000:9000 colormask-backend