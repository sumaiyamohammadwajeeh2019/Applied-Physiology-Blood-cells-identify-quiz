@echo off
REM ============================================================
REM  Blood 10 Cells Puzzle - FULL DEPLOY via Render CLI (Free Static Site)
REM  Run this file: double-click DEPLOY_RENDER_CLI.bat
REM ============================================================
cd /d "%~dp0"
echo.
echo === [0/6] Checking tools ===
git --version || (echo ERROR: Install Git from https://git-scm.com/downloads & pause & exit /b 1)
where render >nul 2>nul
if errorlevel 1 (
  echo Render CLI not found - installing via winget...
  winget install render.cli
  echo.
  echo IMPORTANT: Close this window, open a NEW terminal, then re-run this file.
  pause
  exit /b 1
)
echo Git + Render CLI OK.
echo.

echo === [1/6] Init git repo if needed ===
if not exist ".git" (
  git init
  git branch -M main
  echo git init done.
) else (
  echo .git already exists.
)
echo.

echo === [2/6] Adding ONLY live files (images + html + yaml) ===
git add index.html 10cells.jpg real1.webp real2.webp real3.webp real4.webp real5.webp real6.webp real7.webp real8.webp real9.webp real10.webp render.yaml .gitignore README_RENDER.md
git status --short
git commit -m "blood puzzle static site for Render free" 2>nul
echo.

echo === [3/6] Connect to GitHub ===
git remote -v | findstr origin >nul
if errorlevel 1 (
  echo No origin remote. Enter your GitHub repo URL:
  echo Example: https://github.com/sumaiyamohammadwajeeh2019/Applied_physiology_blood-cells-.git
  set /p REPO_URL="Paste repo URL and press Enter: "
  git remote add origin %REPO_URL%
) else (
  git remote -v
)
echo Pushing to GitHub (login in browser if asked)...
git push -u origin main
if errorlevel 1 (
  echo.
  echo PUSH FAILED. Fix: create empty repo on https://github.com/new first,
  echo then re-run this file. Your repo must match the remote URL.
  pause
  exit /b 1
)
echo.

echo === [4/6] Render login (browser opens once) ===
render login
if errorlevel 1 (echo Login failed. Try again. & pause & exit /b 1)
echo.

echo === [5/6] Validate render.yaml ===
render blueprints validate
echo.

echo === [6/6] Launch Blueprint on Render ===
echo This creates the FREE static site from render.yaml...
render blueprint launch --help
echo.
echo ------------------------------------------------------------
echo Run this next (copy-paste). Replace nothing if render.yaml is in repo root:
echo    render blueprint launch --blueprint render.yaml
echo.
echo OR create static site directly (no blueprint):
echo    render services create --help
echo Then pick: Static Site ^> repo=YOUR_REPO ^> branch=main ^> build="echo static" ^> publish=./
echo ------------------------------------------------------------
echo.
echo After first deploy, redeploy anytime with:
echo    render deploys create YOUR_SERVICE_ID --wait --confirm
echo    (get ID via: render services --output json)
echo.
pause
