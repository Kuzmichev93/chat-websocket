import json
import time
from http.server import HTTPServer, BaseHTTPRequestHandler
from socket import gethostbyname, gethostname,getaddrinfo

from Respons import Respons
from Parser import  Parser
#from asi.my_websocket import get_my_ip
def get_my_ip():
    return gethostbyname(gethostname())

class Server(BaseHTTPRequestHandler,Respons):
    def do_GET(self):
        if self.path == '/chat.html':
            self.path.strip('/')
            data = open('./asi/'+self.path.strip('/'),encoding="utf-8")
            text = data.read()
            self.send_response(200)
            self.send_header("Content-type",'text/html')
            self.end_headers()
            self.wfile.write(bytes(text,'utf-8'))

        elif self.path == '/chat_js.js':
            self.path.strip('/')
            data = open('./asi/'+self.path.strip('/'),encoding="utf-8")
            text = data.read()
            self.send_response(200)
            self.send_header("Content-type",'text/js')
            self.end_headers()
            self.wfile.write(bytes(text,'utf-8'))
        elif self.path == '/chat_css.css':
            data = open('./asi/'+self.path.strip('/'),encoding="utf-8")
            text = data.read()
            self.send_response(200)
            self.send_header("Content-type",'text/css')
            self.end_headers()
            self.wfile.write(bytes(text,'utf-8'))


        elif self.path == '/get_my_ip':
            self.send_response(200)
            self.send_header("Content-type",'text/text')
            self.end_headers()
            self.wfile.write(bytes(self.client_address[0],'utf-8'))
        else:
            self.send_error(404,'Not found')


def run(server_class=HTTPServer, handler_class=Server):
    server_address = ('192.168.0.104', 8060)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()



run()