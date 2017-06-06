from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import json
import random
import os
from os import curdir, sep
from mimetypes import types_map

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    #def do_GET(self):
    #    self._set_headers()
    #    f = open("index.html", "r")
    #    self.wfile.write(f.read())
    def do_GET(self):
        #try:
        #    if self.path == "/":
        #        self.path = "/index.html"
        #    if self.path == "favico.ico":
        #        return
        #    fname,ext = os.path.splitext(self.path)
        #    if ext in (".html", ".css"):
        #        #with open(os.path.join(curdir,self.path)) as f:
        #        with open(os.path.join(curdir,self.path)) as f:
        #            self.send_response(200)
        #            self.send_header('Content-type', types_map[ext])
        #            self.end_headers()
        #            self.wfile.write(f.read())
        #    return

        if self.path == "/":
            self.path = "/index.html"

        try:
			#Check the file extension required and
			#set the right mime type

			sendReply = False
			if self.path.endswith(".html"):
				mimetype='text/html'
				sendReply = True
			if self.path.endswith(".jpg"):
				mimetype='image/jpg'
				sendReply = True
			if self.path.endswith(".gif"):
				mimetype='image/gif'
				sendReply = True
			if self.path.endswith(".js"):
				mimetype='application/javascript'
				sendReply = True
			if self.path.endswith(".css"):
				mimetype='text/css'
				sendReply = True

			if sendReply == True:
				#Open the static file requested and send it
				f = open(curdir + sep + self.path) 
				self.send_response(200)
				self.send_header('Content-type',mimetype)
				self.end_headers()
				self.wfile.write(f.read())
				f.close()
			return

        except IOError:
            self.send_error(404)


    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        self._set_headers()
        print "in post method"
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))

        self.send_response(200)
        self.end_headers()

        data = json.loads(self.data_string)
        with open("setupfile.txt", "w") as outfile:
            json.dump(data, outfile)
        print "{}".format(data)
        #f = open("for_presen.py")
        #self.wfile.write(f.read())
        return


def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

if len(argv) == 2:
    run(port=int(argv[1]))
else:
    run()
