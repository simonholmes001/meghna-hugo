#!/usr/bin/env bash

cd /Users/simonholmes/mathisi/alkoho-platform/proteinFolding/structurePrediction/data/

for dir in */
do
    cd ${dir}
#    ls
    for file in ./*
    do
        gzip -d ${file}
        done
    cd ../
    ls
done

for dir in */
do
    cd ${dir}
#    ls
    for file in ./*
    do
        mv ${file} ../*
        done
    cd ../
    ls
done