@echo off
cd /d "%~dp0"
git status
git add index.html 10cells.jpg real1.webp real2.webp real3.webp real4.webp real5.webp real6.webp real7.webp real8.webp real9.webp real10.webp render.yaml .gitignore README_RENDER.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/sumaiyamohammadwajeeh2019/Applied_physiology_blood-cells-.git
git push -u origin main
pause
