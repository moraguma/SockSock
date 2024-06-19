import sys
from socksock.sock_server import SockServer


class Server():
    def hello():
        return {"return": "world!"}


    def add(arg1, arg2):
        return {"return": arg1 + arg2}


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit:
        print("Usage: socksock.examples.example_server <port>")
        exit()
    
    sock_server = SockServer(Server(), int(sys.argv[1]), True)
    sock_server.listen()
