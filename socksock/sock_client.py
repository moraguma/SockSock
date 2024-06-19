import socket
import json


BUFSIZE = 4096


class SockClient():
    def __init__(self, port) -> None:
        self.client_socket = socket.socket()
        self.client_socket.connect((socket.gethostname(), port))
    

    def __getattribute__(self, name: str) -> socket.Any:
        if name == "close":
            return self.close
        
        def call_server(**kwargs):
            self.client_socket.sendall(bytes(json.dumps(kwargs), encoding="utf-8"))
            return json.loads(self.client_socket.recv(BUFSIZE))

        return call_server


    def close(self):
        self.client_socket.close()
        self.client_socket = None