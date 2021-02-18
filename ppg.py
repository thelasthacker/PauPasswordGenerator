import random
import sys
import argparse

class Colors:
   OK = '\033[92m'
   FAIL = '\033[91m'
   BOLD = '\033[1m'
   ENDC = '\0m'
   UNDERLINE = '\033[4m'

print(Colors.BOLD + "__________                                                     ")
print("\______   \_____   __ __                                       ")
print(" |     ___/\__  \ |  |  \                                      ")
print(" |    |     / __ \|  |  /                                      ")
print("_|____|___ (____  /____/                                 .___  ")
print("\______   \_____\/  ______ ________  _  _____________  __| _/  ")
print(" |     ___/\__  \  /  ___//  ___/\ \/ \/ /  _ \_  __ \/ __ |   ")
print(" |    |     / __ \_\___ \ \___ \  \     (  <_> )  | \/ /_/ |   ")
print(" |____|___ (____  /____  >____  >  \/\_/ \____/|__|  \____ |   ")
print(" /  _____/  ____\/ ____\/ ____\/__________ _/  |_  _______\/__ ")
print("/   \  ____/ __ \ /    \_/ __ \_  __ \__  \\   __\/  _ \_  __ \ ")
print("\    \_\  \  ___/|   |  \  ___/|  | \// __ \|  | (  <_> )  | \/ ")
print(" \______  /\___  >___|  /\___  >__|  (____  /__|  \____/|__|    ")
print("        \/     \/     \/     \/           \/                   ")
print("                     V1.0                  By thelasthacker  \n")

alfabet = "abcdefghijklmnopqrstuvwxyz"
alfabet_majus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "0123456789"
signes = "_!()[]~#@*"

def generar_contrasenya(l):
    global contrasenya
    contrasenya = []
    i = 0
    while i<=(l+3):
        if random.randrange(0,3) == 0:
            contrasenya += random.choices(list(alfabet))
        elif random.randrange(0,3) == 1:
            contrasenya += random.choices(list(alfabet_majus))
        elif random.randrange(0,3) == 2:
            contrasenya += random.choices(list(nums))
        elif random.randrange(0,3) == 3:
            contrasenya += random.choices(list(signes))
        i += 1
    return "".join(contrasenya)

def amagar_contrasenya(c):
    cl = list(c)
    for char in cl:
        pos = cl.index(char)
        if char == "a":
            cl[pos] = "4"
        elif char == "e":
            cl[pos] = "3"
        elif char == "i" or char == "l":
            cl[pos] = "1"
        elif char == "o":
            cl[pos] = "0"
        elif char == "s":
            cl[pos] = "5"
        
        else:
            pass

    return "".join(cl)

def get_arguments():
    parser = argparse.ArgumentParser(description="Generar contrasenyes segures")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-s", "--size", dest="tamany", type=int, help="Especifica el nombre caracters de la contrasenya")
    group.add_argument("-H", "--hide", dest="amagar", type=str, help="Especifica la contrasenya que vols camuflar o amagar substituint lletres per numeros")

    return parser.parse_args()

args = get_arguments()

if args.tamany:
    tamany = args.tamany

    print("\n[~] Obtenint els caracters...")
    print(Colors.OK + "\n[+] Contrasenya generada: " + str(generar_contrasenya(tamany)) + "\n")
elif args.amagar:
    global contrasenya
    contrasenya = args.amagar

    print("\n[~] Obtenint els caracters...")
    print(Colors.OK + "\n[+] Contrasenya amagada: " + str(amagar_contrasenya(contrasenya)) + "\n") 
   
