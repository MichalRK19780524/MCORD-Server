#!/usr/bin/python
import socket
import sys
import json
HOST, PORT = "127.0.0.1", 5555
data = " ".join(sys.argv[1:])
class client:
   def __init__(self,host,port):
     self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     self.sock.connect((host,port))
     #Receive the greeting string
     r=""
     self.sockFile = self.sock.makefile()
     c=self.sockFile.readline()
     print(c)
   def do_cmd(self,obj):
     self.sock.sendall((json.dumps(obj)+"\n").encode("utf8"))
     res = self.sockFile.readline()
     res = json.loads(res)
     return res

cli=client(HOST,PORT)