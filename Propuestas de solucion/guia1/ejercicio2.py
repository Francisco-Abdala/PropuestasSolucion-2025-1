def main():
    #Pide dos números al usuario.
    numero1 = float(input("Ingrese un número:"))
    numero2 = float(input("Ingrese otro número:"))

    #Realiza la suma.
    resultado = numero1 + numero2
    #Muestra el resultado de la suma.
    print(f"El resultado de la suma de {numero1} y {numero2} es: {resultado}")

if __name__ == "__main__":
    main()