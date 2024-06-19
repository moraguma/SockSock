import sys
from socksock.sock_client import SockClient


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit:
        print("Usage: socksock.examples.example_client <port>")
        exit()
    
    sock_client = SockClient(int(sys.argv[1]))
    
    x = [""]
    while x[0] != "quit":
        print("\nCOMMANDS\nhello\nadd arg1 arg2\n\n")
        x = input().split(" ")

        if len(x) == 0:
            print("\nPlease type a command\n")
            x = [""]
            continue

        match x[0]:
            case "hello":
                sock_client.hello()
            case "add":
                if len(sock_client) != 3:
                    print("\nSyntax - add arg1 arg2\n")
                    continue
                sock_client.add(x[1], x[2])
            case "quit":
                pass
            case _:
                print("\nUnrecognized command\n")
