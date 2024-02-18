#!/usr/bin/env python3
import socket
import threading
HOST = 'localhost'
PORT = 1234

class ClientThread(threading.Thread):

    def __init__(self, client_sock, client_addr):
        super().__init__()
        self.client_sock = client_sock
        self.client_addr = client_addr

        print(f"[+] Nuevo cliente conectado: {client_addr}")

    def run(self):
    
        message = ''

        while True:
            data = self.client_sock.recv(1024)
            message = data.decode()

            #pdb.set_trace() --> Hace un debbugin

            if message.strip() == 'bye':
                break
            print(f"\n[+] Mensaje mandado por el cliente: {message.strip}")
            self.client_sock.send(data) #Para mensajes cortos
        print(f"[+] Cliente {client_addr} desconectado")
        self.client_sock.close()




with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:

    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #1: Nivel de socket(SOL_SOCKET--> nivel de socket o el socket principal (Otras opciones: IPPROTO_IP, IPPROTO_TCP, IPPROTO_UDP)) 2: :
    server_socket.bind((HOST, PORT))
    print("[+] En espera de conexiones...")

    while True:

        server_socket.listen()
        client_sock, client_addr = server_socket.accept()
        new_thread = ClientThread(client_sock, client_addr)    
        new_thread.start() #run 
