import sys
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import asyncio
from multiprocessing import Process, current_process

PARALLEL_PROCESSES = 2

class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type','text/html')
    self.end_headers()
    self.wfile.write(str(current_process().pid).encode())
    return

def server(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler, port=8000):
  print("Starting " + str(port))
  server_address = ('', int(port))
  httpd = server_class(server_address, handler_class)
  httpd.serve_forever()
if __name__ == '__main__':
  processes = [Process(target=server, args=(HTTPServer, handler, 8000+i)) for i in range(PARALLEL_PROCESSES)]
  for process in processes:
    process.start()
