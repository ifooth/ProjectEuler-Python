@echo off
cls
set i=1

:start
set /p input=Console [%i%]:
python -m euler %input%
set /a i+=1
goto start