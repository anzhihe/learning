#!/bin/bash

cp ~/anaconda-ks.cfg data.txt
file=data.txt
head $file

# 要插入的头的内容
title="***This is the title line of data text file***"
echo $title | cat - $file > $file.new

head data.txt.new
exit 0
