#!/usr/bin/python
import socket
import json


class Connection:
    PORT = 5555

    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        self.sockFile = self.sock.makefile()

    def do_cmd(self, obj):
        self.sock.sendall((json.dumps(obj)+"\n").encode("utf8"))
        res = self.sockFile.readline()
        res = json.loads(res)
        return res
