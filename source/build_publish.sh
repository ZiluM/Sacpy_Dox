#!/usr/bin/env bash

cd ../
make clean
make html
cd source
rm -rf ../docs/*
cp -r ../build/html/* ../docs
git add ../docs
