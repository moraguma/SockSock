import sys
from socksock.sock_server import SockServer


class Server():
    def hello(self):
        return {"return": "world!"}


    def add(self, arg1, arg2):
        return {"return": arg1 + arg2}


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit:
        print("Usage: socksock.examples.example_server <port>")
        exit()
    
    sock_server = SockServer(Server(), int(sys.argv[1]), True)
    try:
        sock_server.listen()
    except KeyboardInterrupt:
        sock_server.close()
