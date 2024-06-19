import socket
import json


BUFSIZE = 9192

class SockServer():
    def __init__(self, server, port, verbose=False) -> None:
        """
        Receives the object that will respond to the calls received by this server
        """
        self.server = server
        self.port = port
        self.verbose = verbose
        
        self.server_socket = socket.socket()
        self.server_socket.bind((socket.gethostname(), port))

        self.listening = False
    

    def close(self) -> None:
        """
        Stop processing calls
        """
        self.print_verbose("Closing sockets")
        self.server_socket.close()
        self.server_socket = None
        self.listening = False


    def listen(self) -> None:
        """
        Start listening to calls on its port. Will forward them to server
        """
        self.server_socket.listen(0)
        while True:
            self.print_verbose(f"Listening on port {self.port}")
            conn, address = self.server_socket.accept()
            while True:
                data = conn.recv(BUFSIZE)
                if not data: break

                try:
                    data_dict = json.loads(data)

                    if self.check_respond_print(conn, len(self.check_missing_fields(data_dict, ["method", "args"])) != 0, f"Calls must include method and args fields. Received {list(data_dict.keys())}"): continue
                    if self.check_respond_print(conn, not callable(getattr(self.server, data_dict["method"], None)), f"Tried to call unrecognized method {data_dict['method']}"): continue

                    self.send_json_to_client(conn, getattr(self.server, data_dict["method"])(**data_dict["args"]))
                except Exception as e:
                    self.send_json_to_client(conn, {"info": f"Exception - {e}"})
    

    def check_respond_print(self, conn, condition, message):
        """
        If the given condition is true, responds to the client with the given message, prints it and returns true. Otherwise, returns false
        """
        if condition:
            self.send_json_to_client(conn, {"info": message})
            self.print_verbose(f"Error during call - {message}")
            return True
        return False



    def check_missing_fields(self, data_dict, fields):
        """
        Return a list that contains every field in fields not present in dictionary
        """
        missing_fields = []
        for field in fields:
            if not field in data_dict: 
                missing_fields.append(field)
        return missing_fields


    def send_json_to_client(self, conn, data_dict):
        conn.sendall(bytes(json.dumps(data_dict), encoding="utf-8"))


    def print_verbose(self, value):
        if self.verbose:
            print(value)


            



