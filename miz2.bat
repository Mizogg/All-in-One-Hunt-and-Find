@Echo off
title Mizogg.co.uk
Pushd "%~dp0"
:loop
python bchr.py
goto loop