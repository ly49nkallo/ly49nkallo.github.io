#!/usr/bin/env python3
"""Start a local HTTP server for previewing the site at http://localhost:8000"""

import http.server
import socketserver
import webbrowser

PORT = 8000

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    print("Press Ctrl+C to stop.")
    webbrowser.open(f"http://localhost:{PORT}")
    httpd.serve_forever()
