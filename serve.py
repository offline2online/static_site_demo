#!/usr/bin/env python3
import os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '')
from http.server import SimpleHTTPRequestHandler, HTTPServer
print("Serving at http://localhost:3456", flush=True)
HTTPServer(('', 3456), SimpleHTTPRequestHandler).serve_forever()
