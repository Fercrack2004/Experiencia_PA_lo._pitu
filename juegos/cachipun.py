import random
def cachipun():
    print("ca")
    print("chi")
    print("pun")
    eleccion = input()
    mierda = random.randint(1,3)
    if eleccion == "tijera":
        if mierda == 1:
            return str("tijera, empataste")
        elif mierda == 2:
            return str("piedra, perdiste")
        elif mierda == 3:
            return str("papel, ganaste")
        
    elif eleccion == str("piedra"):
        if mierda == 1:
            return str("tijera, ganaste")
        elif mierda == 2:
            return str("piedra, empataste")
        elif mierda == 3:
            return str("papel, perdiste")
    
    elif eleccion == str("papel"):
        if mierda == 1:
            return str("tijera, perdiste")
        elif mierda == 2:
            return str("piedra, ganaste")
        elif mierda == 3:
            return str("papel, empataste")
    pass
print(cachipun())