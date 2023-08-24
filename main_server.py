from http.server import HTTPServer, BaseHTTPRequestHandler

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', 'http://localhost')
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'¡Hola desde el servidor!')

def run():
    address = ('', 8000)
    server = HTTPServer(address, MyRequestHandler)
    print('Servidor corriendo en http://localhost:8000')
    server.serve_forever()

if __name__ == '__main__':
    run()
