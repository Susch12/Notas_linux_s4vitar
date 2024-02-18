#!/usr/bin/env python3

import socket

def start_socket():

    host = 'localhost'
    port = 1234

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as a:

        a.connect((host, port))

        while True:

            message = input("\n[+] Introduce tu mensaje: ")
            a.sendall(message.encode())

            if message == 'bye':
                break

            data = a.recv(1024)

            print(f"\n[+] Mensaje del servidor: {data.decode()}")


start_socket()
