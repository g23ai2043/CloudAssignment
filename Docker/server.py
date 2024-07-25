from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # Serve files from the "templates" directory if the path is "/"
        if path == '/':
            path = '/templates/index.html'
        return super().translate_path(path)

def run(server_class=HTTPServer, handler_class=CustomHTTPRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()