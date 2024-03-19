#!/usr/bin/env python3

import argparse
import re


def is_validate(interface, mac_address):

    is is_validate = re.match(r'^[]$', interface)

def get_argument():
    parse = argparse.ArgumentParser(description="Herramienta para cambiar la dirección MAC de una interfaz de red")
    parse.add_argument("-i", "--interface", required = True, dest='interface',help="Nombre de la interfaz de red")
    parse.add_argument("-m", "--mac", required = True, dest="mac_address", help="Nueva dirección para la interfaz de red")

    return parse.parse_args()


def change_mac_address(interface, mac_address):

    if is_validate(interface, mac_address)

def main():
    args = get_argument()
    
    change_mac_address(args.interface, args.mac_address)

if __name__ == '__main__':
    main()
