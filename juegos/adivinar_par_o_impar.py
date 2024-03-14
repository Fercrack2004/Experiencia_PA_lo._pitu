import random
def adivinar_par_o_impar():
    n = input("¿El numero sera par o impar? Elige 1 para impar y 2 para par")
    par = False
    a = random.randint(1,10)
    if a%2==0:
        par = True
    if n!="1" and n!="2":
        print("Input no valido")
        return
    elif n == "1":
        if par==False:
            print("Wow! Adivinaste, el numero es impar!")
            return
        else:
            print("Goofy ah, el numero es par 'laughing emoji'")
            return
    elif n=="2":
        if par==True:
            print("Wow! Adivinaste, el numero es par!")
            return
        else:
            print("Goofy ah, el numero es impar 'laughing emoji'")
            return
adivinar_par_o_impar()
    