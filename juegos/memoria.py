import random
import time
def memoria():
    """
    Esta función representa el juego de memoria.
    Debes generar una secuencia de números al azar y mostrarla al usuario.
    Luego, debes pedir al usuario que repita la secuencia.
    Se debe mostrar un mensaje si el usuario acierta o no.
    """
    numero=random.randint(100000000,1000000000)
    print("HEEEEEEEY, mucho ojo, tienes 5 segundos para memorizar este numero, 😨😨😨: ",numero)
    time.sleep(5)
    print(f"🟨🟨🟨🟨⬛\n🟨🟨🟨🟨⬛\n🟨🟨🟨🟨🟨⬛\n🟨🟨🟨🟨🟨🟨⬛⬛\n🟨🟨⬛⬛⬛⬛⬜⬜⬛\n🟨🟨⬛⬜⬜⬛⬜⬜⬜⬛\n🟨⬛⬜⬜⬜⬜⬛⬜⬛⬜⬛\n🟨⬛⬜⬜⬜⬜⬛⬜⬜⬛\n🟨⬛⬜⬜⬛⬜⬜⬛⬛\n🟨🟨⬛⬜⬜⬜⬜⬛🟨⬛\n🟨🟨🟨⬛⬛⬛🟨🟨🟨⬛\n🟨🟨🟨🟨🟨🟨🟨⬛⬛⬛\n🟨🟨🟨🟨🟨⬛⬛⬛⬛⬛\n🟨🟨🟨🟨⬛⬛⬛🟫🟫⬛\n🟨🟨🟨⬛🟫🟫🟫🟫🟫⬛\n🟨🟨⬛🟫🟫🟫🟫🟫🟫🟫⬛\n🟨🟨⬛🟫⬛🟫🟫🟫🟫⬛\n🟨🟨⬛🟫⬛⬛⬛⬛⬛\n🟨🟨⬛🟫🟫🟫⬛\n🟨🟨🟨⬛🟫🟫 Cuando yo la Vi")
    time.sleep(2)
    print("escribe el numero exactamente igual al que viste antes")
    lol=int(input())
    if lol==numero:
        print("HEEEEEEEEEEEEY, eres un genio, felicidades shinji")
    else:
        print("wuawua, que pena, perdiste 👎")
    return
memoria()