from colorama import Fore, init
init(autoreset=True) 

def exito(msg):
    print(Fore.GREEN + msg)

def error(msg):
    print(Fore.RED + msg)

def alerta(msg):
    print(Fore.YELLOW + msg)