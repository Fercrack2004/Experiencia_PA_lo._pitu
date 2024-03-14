import random
n = random.randint(1,10)

def adivinar_numero():
    a = False
    while a == False:
        print("elige un numero del 1 al 10 y presiona enter")
        b = int(input())
        if b == n:
            print("CORRECTOOOOOOOOOOOOOO")
            break
        else:
            print("incorrecto, intentalo de nuevo")
    pass
adivinar_numero()