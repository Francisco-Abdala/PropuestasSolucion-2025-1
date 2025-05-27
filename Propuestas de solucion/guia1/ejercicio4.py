def main():
    #Se pide un número al usuario.
    numerote = int(input("Ingrese un número"))

    #Comprueba si el resto de la división del número ingresado con 2 es igual a cero.
    if numerote % 2 == 0:
        print(f"El número {numerote} es par")
    else:
        print(f"El número {numerote} es impar")

if __name__ == "__main__":
    main()