#!/bin/bash

echo -e "[+] Esta es tu direccion ip privada -> $(ip a | grep ens33| tail -n 1| awk '{print $2}'| awk '{print $1}' FS="/")" 

# tail es para quedarse con la ùltima linea tambièn puede hacerse con awk 'NR==2' para seleccionara la sgunda linea
# con awk se escoge el segundo argumento y se imprime
# Para concluir tambièn puedes concluir con awk '{print $1}' FS='/' --> FS es el delimitador. --> Tambièn se puede realizar con   cut -d '/' -f 1   --> Tambien se puede realizar con tr '/' ' ' | awk '{print $1}'
# -e para que acepte todos tipos de caracteres especiales.


