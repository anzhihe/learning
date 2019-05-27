#!/bin/sh

rm yorserver.spec
rm -rf dist/yorserver
rm -rf ../bin/*
python /home/install/pyinstaller-2.0/pyinstaller.py yorserver.py
python /home/install/pyinstaller-2.0/pyinstaller.py yorserver.spec
cp pubutil.pyc ../bin/ 
cp dist/yorserver/* ../bin/ 
cp -R cgi-bin ../bin/
rm -rf build
rm -rf logdict2.6.6.final.0-1.log
chmod +x ../bin/cgi-bin/*