import random
def verificar_numero():
    es_numero = False
    numerote = 0
    while es_numero != True:
        palabra = input("Ingrese un número: ")
        if palabra.isnumeric():
            numerote = int(palabra)
            if numerote >= 1 and numerote <= 3:
                break
        else:
            print("\t Ingrese un número válido.")
    return numerote

def main():
    #Se crea la lista con las opciones.
    opciones = ["Piedra","Tijeras","Papel"]
    print("\t Bienvenido al cachipún, ingrese su opción: \n (1) Piedra \n (2) Tijeras \n (3) Papel")
    numero = verificar_numero()
    numerillo = random.randint(0,2)
    opcion_jugador = opciones[numero-1]
    opcion_pc = opciones[numerillo]
    #Se comprueba las posibles combinaciones de jugadas.
    if opcion_jugador == "Piedra" and opcion_pc == "Tijeras":
        print("\tGanó el jugador.")
    elif opcion_jugador == "Piedra" and opcion_pc == "Papel":
        print("\tPerdió el jugador.")
    elif opcion_jugador == "Tijeras" and opcion_pc == "Papel":
        print("\tGanó el jugador.")
    elif opcion_jugador == "Tijeras" and opcion_pc == "Piedra":
        print("\tPerdió el jugador")

    elif opcion_jugador == "Papel" and opcion_pc == "Piedra":
        print("\t Ganó el jugador.")
    elif opcion_jugador == "Papel" and opcion_pc == "Tijeras":
        print("\tPerdió el jugador")


if __name__ == "__main__":
    main()