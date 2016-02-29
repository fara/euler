#!/usr/bin/env python

'''Respond to HTTP requests with pages containing information about those requests.'''

import BaseHTTPServer

# Create a class to handle requests.  Documentation says that __init__
# should not need overriding or extending.  Request method XYZ is
# handled by method do_XYZ; all information is passed via instance
# variables.

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    # Page to send back.
    Page = '''\
<html>
<body>
<p>Hello, Nitinat!</p>
</body>
</html>
'''

    # Handle a GET request.
    def do_GET(self):
        self.sendPage()

    # Handle a POST request.
    def do_POST(self):
        self.sendPage()

    # Send the page.
    def sendPage(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(len(self.Page)))
        self.end_headers()
        self.wfile.write(self.Page)

#----------------------------------------------------------------------
# Create and run the server

if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = BaseHTTPServer.HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()
