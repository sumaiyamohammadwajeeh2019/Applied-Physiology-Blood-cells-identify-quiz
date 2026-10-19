"""Start Flask app.py in background and print live URLs + route checks."""
import subprocess, sys, time, pathlib, urllib.request
HERE = pathlib.Path(__file__).parent
PORT = 10000

# kill anything old on the port is left to user; just start fresh
proc = subprocess.Popen([sys.executable, str(HERE / "app.py")],
                        cwd=str(HERE),
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print(f"Flask PID: {proc.pid} - waiting for http://localhost:{PORT}/ ...")
ok = False
for _ in range(30):
    time.sleep(1)
    try:
        with urllib.request.urlopen(f"http://localhost:{PORT}/healthz", timeout=3) as r:
            body = r.read().decode()
            print(f"/healthz {r.status}: {body}")
            ok = True
            break
    except Exception as e:
        print(f"waiting... ({e})")
if not ok:
    print("Server did not start. Run 'python app.py' manually to see errors.")
    sys.exit(1)

for path in ["/", "/healthz", "/privacy", "/terms", "/manifest.json",
             "/manifest.webmanifest", "/sw.js", "/worker.js", "/robots.txt",
             "/sitemap.xml", "/icon-192.png", "/real1.webp", "/index.html"]:
    try:
        with urllib.request.urlopen(f"http://localhost:{PORT}{path}", timeout=5) as r:
            print(f"GET {path} -> {r.status} ({len(r.read())} bytes)")
    except Exception as e:
        print(f"GET {path} FAILED: {e}")

print()
print(f"OPEN: http://localhost:{PORT}/  (quiz)")
print(f"OPEN: http://localhost:{PORT}/privacy  (privacy policy)")
print("Server running in background. To stop: kill the Python process or close terminal.")
print(f"PID: {proc.pid}")
