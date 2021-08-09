@Echo off
title Mizogg.co.uk
Pushd "%~dp0"
start miz1.bat
start miz2.bat
start miz3.bat
start miz4.bat
start miz5.bat
:loop
python mizbit3.py
goto loop