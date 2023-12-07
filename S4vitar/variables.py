#!/usr/bin/env python3

ip_adress = "192.168.1.181"
print(ip_adress)
print(type(ip_adress))

port = 80
print(port)
print(type(port))

number = 2.15
print(number)
print(type(number))

number_float = float(2) #Cast de variables
print(number_float)
print(type(number_float))

print("---------------------------------------- LISTAS ------------------------------------------------------------- ")

my_ports = []
my_ports.append(22)
my_ports.append(80)
my_ports.append(444)
# Imprimir de forma ineficiente
print(my_ports[0])
print(my_ports)
#Forma de imprimir con condicionales
for port in my_ports:
    print(f"Puerto: {port}") # Forma de combianr un entero con un str


