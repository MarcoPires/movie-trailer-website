#SimpleHTTPServer python server 
#only to simplify access
import app
import sys
import webbrowser;
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
from random import randint


ServerClass  = BaseHTTPServer.HTTPServer
Protocol     = "HTTP/1.0"

class HandlerClass(SimpleHTTPRequestHandler):
	
	def end_headers(self):
		self.send_header("Access-Control-Allow-Origin", "*")
		SimpleHTTPRequestHandler.end_headers(self);


if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = randint(1000,9999)
server_address = ('localhost', port)

HandlerClass.protocol_version = Protocol
httpd = ServerClass(server_address, HandlerClass)

sa = httpd.socket.getsockname()
print "Serving HTTP on", sa[0], "port", sa[1], "..."
webbrowser.open("http://localhost:"+str(port))

try:
	httpd.serve_forever()
except KeyboardInterrupt:
	pass
httpd.server_close()