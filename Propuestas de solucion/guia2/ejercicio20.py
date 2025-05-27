def adivinar_palabra():
    #Se crea la lista que almacenará cada letra de la palabra a adivinar.
    TOGUESS = []
    PALABRA = "bioinformatica"
    for letra in PALABRA:
        TOGUESS.append(letra.lower())
    return TOGUESS

def longitud_palabra():
    #Se condiciona a que solo sea capaz de ingresar una sola letra.
    while True:
        usuario = input("Ingrese su letra: ").lower()
        if len(usuario) > 1:
            print("Ingrese una sola letra.")
        else:
            return usuario
        
def mostrar_progreso(palabra, letras_adivinadas):
    progreso = ""
    #Se recorre la palabra.
    for letra in palabra:
        #Si la letra se encuentra en la lista de letras adivinadas, se muestra cuales ha adivinado.
        if letra in letras_adivinadas:
            progreso += letra + " "
        else:
            progreso += "_ "
    return progreso

def main():
    palabra = adivinar_palabra()
    letras_adivinadas = []
    intentos_maximos = 6
    intentos_restantes = intentos_maximos

    print("¿Serás capaz de adivinar la palabra oculta?")
    while intentos_restantes > 0:

        print("Palabra:", mostrar_progreso(palabra, letras_adivinadas))
        print("Intentos restantes:", intentos_restantes)

        letra_usuario = longitud_palabra()
        #Comprueba que no haya ingresado una letra que ya haya ingresado.
        if letra_usuario in letras_adivinadas:
            print("Ya intentaste con esa letra.\n")
            continue
        
        letras_adivinadas.append(letra_usuario)
        #Verifica si la letra ingresada está en la palabra.
        if letra_usuario in palabra:
            print("La letra está en la palabra.\n")
        else:
            #Disminuye la cantidad de intentos disponibles.
            print("La letra no está en la palabra.\n")
            intentos_restantes =  intentos_restantes - 1
        #Se verifica que se cumpla todas las condiciones puestas en la función all().
        if all(letra in letras_adivinadas for letra in palabra):
            print("Adivinaste la palabra:", "".join(palabra))
            return

    print("La palabra era: ", "".join(palabra))

if __name__ == "__main__":
    main()