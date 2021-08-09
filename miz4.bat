@Echo off
title Mizogg.co.uk
Pushd "%~dp0"
:loop
python VIP_KEYS.py
goto loop