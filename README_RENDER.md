# 🩸 Blood 10 Cells Puzzle — Deploy on Render FREE (Static Site)

This folder is a **100% static site** — perfect for Render Free:
- ✅ No sleep (static sites stay online, only free Web Services sleep)
- ✅ Free TLS + global CDN
- ✅ No build step needed

## Files that go LIVE (must stay in repo root)
```
index.html        ← entry point
10cells.jpg       ← intro poster (referenced by index.html)
real1.webp … real10.webp   ← quiz images (referenced as realN.webp)
render.yaml       ← Blueprint for Render
```

## Files that do NOT deploy (now in .gitignore)
`*.docx`, `*_orig.webp`, `10cells.webp`, `cell_raw.webp`, `*.py`, `*.bat`, `tmp.txt`

## Deploy steps (5 min, free)

### Option A — Dashboard (easiest, recommended)
1. Push this folder to GitHub:
```bat
git init
git add index.html 10cells.jpg real1.webp real2.webp real3.webp real4.webp real5.webp real6.webp real7.webp real8.webp real9.webp real10.webp render.yaml .gitignore
git commit -m "blood puzzle static site"
git branch -M main
git remote add origin https://github.com/YOUR_USER/YOUR_REPO.git
git push -u origin main
```
Or just double-click `PUSH_GITHUB.bat` (edit repo URL inside first).

2. Go to https://dashboard.render.com → **New + → Static Site** → connect your repo.
3. Settings:
   - **Branch:** `main`
   - **Build Command:** `echo "static site - no build needed"`
   - **Publish Directory:** `./`
4. Click **Create Static Site**. Done — you get `https://blood-10-cells-puzzle.onrender.com`.

### Option B — Blueprint (render.yaml)
1. Push all files (including `render.yaml`) to GitHub.
2. Dashboard → **New + → Blueprint** → select repo → Render reads `render.yaml` and creates the static site.

## render.yaml (already fixed in this folder)
```yaml
services:
  - type: web
    name: blood-10-cells-puzzle
    runtime: static
    branch: main
    buildCommand: echo "static site - no build needed"
    staticPublishPath: ./
```

## Important notes
- Filenames are **case-sensitive on Render (Linux)** — `index.html` uses lowercase `real1.webp` … `real10.webp` + `10cells.jpg`. Do NOT rename to `.JPG`/`.WEBP`.
- Keep images < ~300 KB each if possible (yours are 168–283 KB ✅).
- Every `git push` to `main` auto-redeploys.
- Custom domain: free (Dashboard → Settings → Custom Domain).
- No `Procfile` / `requirements.txt` / `Dockerfile` needed — those are only for Web Services (which sleep on free). Do NOT create them.

## Test locally before pushing
Double-click `RUN_LOCAL.bat` or run `python run_local.py` → http://localhost:8000/index.html
