from http.server import HTTPServer, SimpleHTTPRequestHandler

# Define the port for your Python server
PORT = 8080

# Set up the server handler
Handler = SimpleHTTPRequestHandler

# Create an HTTP server
httpd = HTTPServer(('localhost', PORT), Handler)

# Start the server
print(f'Starting server on localhost:{PORT}')
httpd.serve_forever()