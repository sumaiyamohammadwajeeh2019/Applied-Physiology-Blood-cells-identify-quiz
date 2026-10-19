"""Quick checks: manifest valid, files exist, Flask app imports, PWA tags in index.html."""
import json, pathlib, sys
HERE = pathlib.Path(__file__).parent
fails = []

def check(name, cond, hint=""):
    print(("PASS " if cond else "FAIL ") + name + (f" - {hint}" if hint and not cond else ""))
    if not cond:
        fails.append(name)

# 1. required files
for f in ["index.html", "app.py", "requirements.txt", "manifest.json", "manifest.webmanifest",
          "sw.js", "worker.js", "privacy.html", "terms.html", "robots.txt", "sitemap.xml",
          "icon-192.png", "icon-512.png", "render.yaml",
          "10cells.jpg", "real1.webp", "real10.webp"]:
    check(f"exists:{f}", (HERE / f).exists())

# 2. manifest valid JSON + icons point to real files
for mf in ["manifest.json", "manifest.webmanifest"]:
    try:
        data = json.loads((HERE / mf).read_text(encoding="utf-8"))
        ok = bool(data.get("name")) and bool(data.get("icons"))
        icons_ok = all((HERE / i["src"]).exists() for i in data.get("icons", []))
        check(f"manifest-valid:{mf}", ok and icons_ok, "name/icons missing or icon file missing")
    except Exception as e:
        check(f"manifest-valid:{mf}", False, str(e))

# 3. sw + worker identical logic (both define same CACHE)
sw = (HERE / "sw.js").read_text(encoding="utf-8")
wk = (HERE / "worker.js").read_text(encoding="utf-8")
check("sw-has-cache", "blood-puzzle-v1" in sw and "addAll" in sw)
check("worker-has-cache", "blood-puzzle-v1" in wk and "addAll" in wk)

# 4. index.html has PWA hooks
idx = (HERE / "index.html").read_text(encoding="utf-8")
check("index-manifest-link", "manifest.webmanifest" in idx)
check("index-sw-register", "serviceWorker" in idx and "sw.js" in idx)
check("index-privacy-link", "privacy.html" in idx)

# 5. Flask app imports + routes exist
try:
    sys.path.insert(0, str(HERE))
    import app as appmod
    rules = sorted({str(r) for r in appmod.app.url_map.iter_rules()})
    for r in ["/healthz", "/privacy", "/terms", "/manifest.json", "/sw.js", "/robots.txt"]:
        check(f"flask-route:{r}", any(x.startswith(r) for x in rules), f"rules={rules}")
    # test client
    c = appmod.app.test_client()
    check("GET /healthz 200", c.get("/healthz").status_code == 200)
    check("GET / 200", c.get("/").status_code == 200)
    check("GET /privacy 200", c.get("/privacy").status_code == 200)
    check("GET /manifest.json 200", c.get("/manifest.json").status_code == 200)
    check("GET /sw.js 200", c.get("/sw.js").status_code == 200)
except Exception as e:
    check("flask-import", False, str(e))

print()
if fails:
    print(f"{len(fails)} FAILED: {fails}")
    sys.exit(1)
print("All checks passed.")
