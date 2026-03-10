#!/usr/bin/env python3
import http.server
import os

os.chdir('/Users/rgeerdink/Documents/Claude Code/menu-board-demo')
handler = http.server.SimpleHTTPRequestHandler
httpd = http.server.HTTPServer(('', 3456), handler)
print('Serving on http://localhost:3456')
httpd.serve_forever()
