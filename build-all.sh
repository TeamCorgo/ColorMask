#!/usr/bin/env bash
set -Eeuo pipefail
IFS=$'\n\t'

sudo docker compose down
sudo docker compose up --build -d
