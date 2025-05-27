def main():
    #Se pide un numero al usuario.
    Gcelsius = float(input("Ingrese la temperatura en grados celsius: "))

    #Se utiliza la fórmula para convertir de celsius -> fahrenheit.
    Gfahrenheit = (Gcelsius* 9/5) + 32

    #Se muestra la temperatura en grados fahrenheit.
    print(f"La temperatura en grados fahrenheit es: {Gfahrenheit}")

if __name__ == "__main__":
    main()