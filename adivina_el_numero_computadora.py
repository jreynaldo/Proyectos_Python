import random


def adivina_el_numero_computadora(x):
    print("========================================")
    print("        ¡Bienvenido(a) el Juego!        ")
    print("========================================")

    print(f"Seleciona un número entre 1 y {x}: para que la computadora intente adivinar ")

    limite_inferior = 1
    limite_superior = x
    respuesta = ""
    while respuesta != "c":
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior

        respuesta = input(f"Mi Prediccion es {prediccion}. Si es muy alta ingresa (A), Si es muy baja ingresa (A), "
                          f"Si es correcta, ingresa (C)").lower()

        if respuesta == "a":
            limite_superior = prediccion - 1

        elif respuesta == "b":
            limite_inferior = prediccion + 1

    print(f"¡Siiiiiiiiii! La computadora adivinó tu númeroo correctamente: {prediccion}")


adivina_el_numero_computadora(10)
