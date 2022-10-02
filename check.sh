#!/bin/bash

FILE=./images/c1.png
while true
do
  if [[ -f "$FILE" ]]; then
    python3 ./readImage.py
  fi
  sleep 300
done
