"""Blood 10 Cells Puzzle - Flask backend for Render (free Web Service option).

Serves the same static files (index.html, real*.webp, 10cells.jpg) plus:
- /healthz (Render health check)
- /privacy (Google Play / AdSense compliant privacy policy)
- /terms
- /manifest.json, /manifest.webmanifest, /sw.js, /worker.js, /robots.txt

Primary deploy stays STATIC (no sleep). Use this only if you need Python dynamic.
Render Web Service settings: Build `pip install -r requirements.txt`, Start `gunicorn app:app`.
"""
import os
import pathlib
from flask import Flask, send_from_directory, render_template_string

HERE = pathlib.Path(__file__).parent
app = Flask(__name__, static_folder=str(HERE), static_url_path="")

PRIVACY_HTML = (HERE / "privacy.html").read_text(encoding="utf-8") if (HERE / "privacy.html").exists() else "<h1>Privacy Policy</h1>"


@app.route("/healthz")
def healthz():
    return {"status": "ok", "app": "blood-10-cells-puzzle"}, 200


@app.route("/")
def home():
    return send_from_directory(HERE, "index.html")


@app.route("/privacy")
@app.route("/privacy.html")
def privacy():
    return send_from_directory(HERE, "privacy.html")


@app.route("/terms")
@app.route("/terms.html")
def terms():
    return send_from_directory(HERE, "terms.html")


@app.route("/manifest.json")
@app.route("/manifest.webmanifest")
def manifest():
    # serve whichever exists
    fname = "manifest.webmanifest" if (HERE / "manifest.webmanifest").exists() else "manifest.json"
    return send_from_directory(HERE, fname, mimetype="application/manifest+json")


@app.route("/sw.js")
@app.route("/worker.js")
@app.route("/service-worker.js")
def sw():
    fname = "sw.js" if (HERE / "sw.js").exists() else "worker.js"
    return send_from_directory(HERE, fname, mimetype="application/javascript")


@app.route("/robots.txt")
def robots():
    return send_from_directory(HERE, "robots.txt", mimetype="text/plain")


# Fallback: serve any static file (images, icons)
@app.route("/<path:filename>")
def static_files(filename):
    f = HERE / filename
    if f.is_file() and f.resolve().is_relative_to(HERE.resolve()):
        return send_from_directory(HERE, filename)
    return send_from_directory(HERE, "index.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
