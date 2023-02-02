#!/bin/bash

find . | grep -E "(__pycache__)" | xargs rm -rf
python3 -m pip install -r requirements.txt
pre-commit install