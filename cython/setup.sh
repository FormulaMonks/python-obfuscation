#!/bin/bash

set -e
set -x

[[ -d ./app ]] && rm -rf ./app
cp -R ../app .
find . -iname "*.py[co]" -delete
make && make clean-py
