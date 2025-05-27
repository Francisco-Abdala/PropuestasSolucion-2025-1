#Para tener presente los tipos de datos es que se define que palabra es un str. (string = str = cadena de texto)
def contar_vocales(palabra: str):
    vocales = 0
    #Python permite recorrer palabras yendo letra a letra.
    for letra in palabra:
        #Comprueba las vocales. La función lower() es propia de Python y convierte las mayúsculas a minúsculas.
        if letra.lower() == "a" or letra.lower() == "e" or letra.lower() == "i" or letra.lower() == "o" or letra.lower() == "u":
            vocales += 1 # Es lo mismo que vocales = vocales + 1.
    #Retorna la cantidad de vocales contadas.
    return vocales


def main():
    #Se pide una palabra, se ejecuta la función y entrega la información pedida.
    ingreso = input("Ingrese una palabra: ")
    total_vocales = contar_vocales(palabra=ingreso)
    print(f"La palabra {ingreso} contiene {total_vocales} vocales.")



if __name__ == "__main__":
    main()