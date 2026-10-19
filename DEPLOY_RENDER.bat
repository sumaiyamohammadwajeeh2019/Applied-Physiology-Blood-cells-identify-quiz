@echo off
cd /d "%~dp0"
echo === Render CLI Deploy: Blood 10 Cells Puzzle ===
echo.
where render >nul 2>nul
if errorlevel 1 (
  echo [1/4] Installing Render CLI via winget...
  winget install render.cli
  echo Re-open terminal after install, then re-run this bat.
  pause
  exit /b
)
echo [1/4] Render CLI found.
echo [2/4] Logging in (browser opens)...
render login
echo [3/4] Validating render.yaml...
render blueprints validate
echo [4/4] Pushing live files to GitHub...
echo.
echo Now create service in dashboard OR via CLI:
echo   render services create --help
echo   - OR open https://dashboard.render.com ^> New ^> Static Site
echo   - Repo: sumaiyamohammadwajeeh2019/Applied_physiology_blood-cells-
echo   - Branch: main, Publish dir: ./, Build: echo static
echo To trigger redeploy later: render deploys create YOUR_SERVICE_ID --wait --confirm
pause
