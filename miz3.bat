@Echo off
title Mizogg.co.uk
Pushd "%~dp0"
:loop
python FR.py
goto loop