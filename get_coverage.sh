#!/bin/bash

mkdir -p coverage

SUMMARY="$(python3 -m pytest --cov=tests)"
result="$(echo "$SUMMARY" | tail -4 | head -1)"


total=($result)
COVERAGE=$(echo ${total[3]})

# save in a json file
jq -n --arg cov "$COVERAGE" \
  --arg lab "$LABEL" \
  '{coverage: $cov}' >"coverage/coverage.json"

# change coverage on readme.md
python3 utils/get_coverage.py