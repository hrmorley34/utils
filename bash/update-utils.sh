#!/bin/sh

# Go to folder containing this file
cd "${0%/*}"

# Only try to fast-forward pull; otherwise prompt user
if git pull --ff-only; then
  : # Success!
else
  echo "Failed fast-forward; merge manually" 1>&2
  exit 1
fi
