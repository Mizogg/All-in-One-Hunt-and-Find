@Echo off
title Mizogg.co.uk
Pushd "%~dp0"
:loop
python r2.py
goto loop