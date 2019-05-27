cd D:\python\OManager\OManager
d:
rd /S /Q dist
rd /S /Q build
del logdict2.7.3.final.0-1.log
python d:/soft/pyinstaller-2.0/pyinstaller.py --onedir -w --icon=img/imac.ico OManager.py
copy MD5sum.exe dist\OManager
xcopy /s data dist\OManager\data\
xcopy /s img dist\OManager\img\
xcopy /s Module dist\OManager\Module\
xcopy /s numbers dist\OManager\numbers\
xcopy /s tmp dist\OManager\tmp\
rd /S /Q build
rd /S /Q build
del logdict2.7.3.final.0-1.log