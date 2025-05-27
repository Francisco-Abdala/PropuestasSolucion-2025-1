#Se crea la función que calcula el área recibiendo dos parámetros: base y altura.
def calcular_area(num1=0,num2=0):
    return (num1 * num2)/2


def main():
    #Se pide al usuario que ingrese los valores de base y altura.
    base = int(input("Ingrese la base de su triángulo: "))
    altura = int(input("Ingrese la altura de su triángulo: "))

    #El valor que entrega la función calcular_area es almacenada en la variable area.
    area = calcular_area(num1=base,num2=altura)

    #Se entrega el área resultante dado la base y la altura.
    print(f"La área de un triángulo de base {base} y altura {altura} es: {area}")


if __name__ == "__main__":
    main()