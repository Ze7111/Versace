@echo OFF
python3 verscae.py %1 %2 %3 %4 %5 %6 %7 %8 %9
if %ERRORLEVEL% neq 0 goto ProcessError


echo Error: %ERRORLEVEL%
exit /b 0

:ProcessError
python verscae.py %1 %2 %3 %4 %5 %6 %7 %8 %9
exit /b 0