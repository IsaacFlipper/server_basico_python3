import http.server
import socketserver
import os

folder = os.path.dirname(__file__)

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
	def do_GET(self):
		if self.path == '/':
			self.path=os.path.join(folder, 'index.html')

		return http.server.SimpleHTTPRequestHandler.do_GET(self)

handler_object = MyHttpRequestHandler

PORT = 80
HOST = 'localhost'
'''
Com o PORT 80 voce pode colocar no navegador so o 'localhost' sem as aspas
mais se voce muda o PORT voce tem que colocar 'localhost:PORT' sem as aspa e o numero correspondente ao PORT
'''
my_server = socketserver.TCPServer((HOST, PORT), handler_object)
print('digite no seu navegador:')
print(f'{HOST}:{PORT}', end=' ')
if PORT == 80:
    print(f'{HOST}')

my_server.serve_forever()
