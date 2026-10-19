import app as A
print("Flask routes:")
for r in sorted(A.app.url_map.iter_rules(), key=str):
    print(" ", r, sorted(m for m in r.methods if m in ("GET", "POST")))
print("HERE files:", [p.name for p in __import__("pathlib").Path(__file__).parent.iterdir() if p.suffix in (".html", ".py", ".json", ".js")])
