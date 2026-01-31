#!/usr/bin/env bash
set -Eeuo pipefail
IFS=$'\n\t'

sudo docker compose build frontend
sudo docker compose up -d frontend
