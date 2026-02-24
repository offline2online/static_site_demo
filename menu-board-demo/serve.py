import http.server, os
os.chdir('/Users/rgeerdink/Documents/Claude Code/menu-board-demo')
class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, fmt, *a): pass
http.server.HTTPServer(('', 3456), Handler).serve_forever()
