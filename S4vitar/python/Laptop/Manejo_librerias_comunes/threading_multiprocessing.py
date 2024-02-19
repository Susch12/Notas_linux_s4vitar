#!/usr/bin/env python3

import threading
import multiprocessing
import time 
import requests

#print("[!] Ejemplo de threading")
#print("-------------------------------------------")
#def tarea(num_tarea):
 #   print(f"[+] Iniciando el hilo: {num_tarea}")
#    time.sleep(2)
#    print(f"[+] Hilo {num_tarea} finalizada")

#thread1 = threading.Thread(target=tarea, args=(1,)) #args debemos definirla como una tupla
#thread2 = threading.Thread(target=tarea, args=(2,))

#thread1.start()
#thread2.start()

#thread1.join()
#thread2.join()

#print(f"[+] Hilos finalizados")
#print("\n-------------------------------------------\n")

#print("[!] Ejemplo de multiprocessing")
# Recuerdad que esta libreria se usa para aprovechar el poder del cpu y que cada uno de estos utilizará su propio almacenamiento de memoria
#proceso1 = multiprocessing.Process(target=tarea, args=(1,))
#proceso2 = multiprocessing.Process(target=tarea, args=(2,))

#proceso1.start()
#proceso2.start()

#proceso1.join()
#proceso2.join()


#print("[+] Los procesos han concluido exitosamente\n")
def realizar_peticion(url):
    response = requests.get(url)
    print(f"[+] Dominio: [{url}]: {len(response.content)} bytes")


dominios = [
        "https://www.google.com",
        "https://www.xvideos.com",
        "https://www.wikipedia.org",
        "https://www.yahoo.com"
    ]
start_time = time.time()

hilos = []

for url in dominios:
    hilo = threading.Thread(target=realizar_peticion, args=(url,))
    hilo.start()
    hilos.append(hilo)


for hilo in hilos:
    hilo.join()

end_time = time.time()

print(f"\n[+] Tiempo transcurrido: {end_time - start_time}")
