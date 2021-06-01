tasklist | find "RocketLeague.exe"
if %ERRORLEVEL% == 0 (
    python delete.py
) else if %ERRORLEVEL% == 1 (
    python close.py
) else (
    python error.py
)
