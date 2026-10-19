@echo off
cd /d "%~dp0"
echo === Blood Puzzle - Run Locally (Flask app.py) ===
python -m pip install -r requirements.txt
echo.
echo Starting Flask at http://localhost:10000/ ...
echo Routes: /  /healthz  /privacy  /terms  /manifest.json  /sw.js
start http://localhost:10000/
python app.py
pause
