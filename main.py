from colorama import Fore
import pyautogui

def credits():
    print("Naprogramoval Rodrick__")
    print("https://github.com/Rodrickhmmm/ZAVBot")

typer():
    print(Fore.RESET + "[1] Normální cvičení")
    print("[2] Cvičení z papíru")
    print("[3] Lenka kajaka")
    print("[4] Padající písmena")
    print("[4] Petiminutovky/desetiminutovky")
    print("[4] Exit")
    
    try:
        choose = int(input(Fore.CYAN + "Vyber: " + Fore.GREEN))
    except ValueError:
        print("tak jseš kokot?? Vyber číslo!!")
        exit()
    if choose > 5:
        print("vyber od 1 do 4!!!!")
        exit()
    elif choose == 1:
        
    elif choose == 2:
        
    elif choose == 3:
        
    elif choose == 4:
        mainmenu()

def mainmenu():
    print(Fore.CYAN + "--- ZAVBot ---")
    print(Fore.RESET + "[1] Typer")
    print("[2] Nastavení")
    print("[3] Credits")
    print("[4] Exit")
    
    try:
        choose = int(input(Fore.CYAN + "Vyber: " + Fore.GREEN))
    except ValueError:
        print("tak jseš kokot?? Vyber číslo!!")
        exit()
    if choose > 5:
        print("vyber od 1 do 4!!!!")
        exit()
    elif choose == 1:
        typer()
    elif choose == 2:
        settings()
    elif choose == 3:
        credits()
    elif choose == 4:
        exit()

mainmenu()
