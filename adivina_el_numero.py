import random


def advina_el_numero(x):

    print("========================================")
    print("        ¡Bienvenido(a) el Juego!        ")
    print("========================================")
    print("Tu Meta es adivinar el número generado por la computadora")
    numro_aleatorio = random.randint(1, x)  # Número aleatorio entre 1 y x.

    prediccion = 0
    while prediccion != numro_aleatorio:
        prediccion = int(input(f"Adivina un número entre 1y {x}: "))
        if prediccion< numro_aleatorio:
            print("Intenta otra vez. Este numero es muy pequeño.")
        elif prediccion >  numro_aleatorio:
            print("Intenta otra vez. Este numero es muy grand.")
    print(f"¡Felicitaciones! Adivinaste el Número {numro_aleatorio} correctamente")


advina_el_numero(10)