#!/bin/bash

# Creates the basic directory structure for the password audit process

DIRNAME="AD-`date +%Y%m`"
mkdir -p $DIRNAME/analysis
mkdir -p $DIRNAME/hashes
mkdir -p $DIRNAME/raw
mkdir -p $DIRNAME/working

# Populates directories that should be committed to git
echo -e "This directory contains the files for analyzing the \
passwords" > $DIRNAME/analysis/README.md
echo -e "This directory contains the raw hashes from AD" \
     > $DIRNAME/hashes/README.md

echo -e "\n \e[33mDirectories created under $DIRNAME\e[39m \n"
