#!/usr/bin/env python3

import socket 

def start_client_chat():

    HOST = 'localhost'
    PORT = 1234

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((HOST, PORT))

    while True:

        client_message = input(f"[+] Mensaje para enviar al server: ")
        client_socket.send(client_message.encode())

        if client_message == 'bye':
            break
        
        server_message = client_socket.recv(1024).strip().decode()

        print(f"[+] Mensaje del server: {server_message}")

    client_socket.close()

start_client_chat()
