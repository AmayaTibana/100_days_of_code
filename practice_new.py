#!/bin/bash

# Default values
count=3
delay=2

# Parse arguments
while [[ $# -gt 0 ]]; do
  key="$1"
  case $key in
    --count)
      count="$2"
      shift
      shift
      ;;
    --delay)
      delay="$2"
      shift
      shift
      ;;
    *)
      echo "Unknown argument $1"
      exit 1
      ;;
  esac
done

# Print random quotes
for ((i=1; i<=count; i++)); do
  shuf -n 1 quotes.txt   # pick 1 random quote
  sleep "$delay"          # wait before next
done