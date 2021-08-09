@Echo off
title Mizogg.co.uk
Pushd "%~dp0"
:loop
python tronbal.py
goto loop