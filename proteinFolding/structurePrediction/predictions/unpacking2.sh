#!/usr/bin/env bash

cd /Users/simonholmes/mathisi/alkoho-platform/proteinFolding/structurePrediction/data/

for dir in */
do
    cd ${dir}
    for file in ./*
    do
        cp ${file} ../
        done
    cd ../
    ls
done
