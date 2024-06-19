import socket
import json


BUFSIZE = 4096


class SockClient():
    def __init__(self, port) -> None:
        self.client_socket = socket.socket()
        self.client_socket.connect((socket.gethostname(), port))
    

    def call(self, method_name: str, **kwargs):
        self.client_socket.sendall(bytes(json.dumps({"method": method_name, "args": kwargs}), encoding="utf-8"))
        return json.loads(self.client_socket.recv(BUFSIZE))


    def close(self):
        self.client_socket.close()
        self.client_socket = None