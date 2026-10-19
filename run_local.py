from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import webbrowser, pathlib, os
PORT = 8000
HERE = pathlib.Path(__file__).parent
os.chdir(HERE)
print(f"Serving {HERE} at http://localhost:{PORT}/index.html")
print("Images: real1-real10.webp + 10cells.jpg must stay in same folder")
print("Press Ctrl+C to stop")
webbrowser.open(f"http://localhost:{PORT}/index.html")
ThreadingHTTPServer(("127.0.0.1", PORT), SimpleHTTPRequestHandler).serve_forever()
