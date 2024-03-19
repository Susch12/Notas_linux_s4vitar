#!/usr/bin/env python3

from forward_shell import FordwardShell
from termcolor import colored
import signal
import sys

def def_handler(sig, frame):
    print(colored("\n[!] Saliendo...\n", 'red'))
    my_forward_shell.remove_data()
    sys.exit(1)


signal.signal(signal.SIGINT,def_handler)

if __name__ == "__main__":

    my_forward_shell = FordwardShell()
    my_forward_shell.run()
