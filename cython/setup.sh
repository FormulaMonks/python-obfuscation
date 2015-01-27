#!/bin/bash

set -e
set -x

[[ -d ./app ]] && rm -rf ./app
cp -R ../app .
find . -iname "*.py[co]" -delete

for name in $(find . ! -path . -type d); do
    cp Makefile $name/
done

make && make clean-py
