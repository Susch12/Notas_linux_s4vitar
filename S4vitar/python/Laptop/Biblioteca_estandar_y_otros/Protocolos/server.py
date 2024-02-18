#!/usr/bin/env python3

import socket

def start_chat_server():

    HOST = 'localhost'
    PORT = 1234

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #TIME WAIT
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print("[+] Servidor listo para aceptar una conexión...")
    client_conn, client_addr = server_socket.accept()
    print(f"[+] El cliente {client_addr} se ha conectado!")

    while True:

        client_message = client_conn.recv(1024).strip().decode() #funcion para mostrar el mensaje
        print(f"[+] Mensaje del cliente {client_message}")
        if client_message == 'bye':
            break


        server_message = input(f"[+] Mensaje para enviar al cliente: ")
        client_conn.send(server_message.encode())


    
    client_conn.close()

start_chat_server()
