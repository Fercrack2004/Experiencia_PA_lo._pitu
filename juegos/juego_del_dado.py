import random
def juego_del_dado():
    """
    Esta función tiene que pedirle al usuario que aprete enter para que lance un dado.
    Esto genera un número al azar que se le suma a la puntuación del usuario.
    Después el computador también tiene que lanzar un dado.
    El primero en sumar 30 puntos gana.
    """
    sumacomputadora=0
    sumajugador=0
    input("presiona enter para lanzar")
    while sumajugador<30 or sumacomputadora<30:
        dado=random.randint(1,6)
        sumajugador+=dado
        if sumajugador>=30:
            print("tu puntuación es",sumajugador)
            print("ganaste")
            break
        else:
            print("sacaste",dado,",tu puntuacion es",sumajugador)
            dado2= random.randint(1,6)
            sumacomputadora+=dado2
            if sumacomputadora>=30:
                print("la puntuacion de la compuitadora es",sumacomputadora)
                print("perdiste")
                break
            else:
                print("la computadora sacó",dado2,",la puntuacion de la computadora es",sumacomputadora)
                input("presiona enter para lanzar")
                
juego_del_dado()