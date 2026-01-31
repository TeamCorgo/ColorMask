#!/usr/bin/env bash
set -Eeuo pipefail
IFS=$'\n\t'

sudo docker compose build backend
sudo docker compose up -d backend
