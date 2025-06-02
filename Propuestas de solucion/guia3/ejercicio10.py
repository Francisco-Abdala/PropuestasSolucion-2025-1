def sumar():
    num1= int(input("Ingrese un número: "))
    num2 = int(input("Ingrese otro número: "))
    print(f"La suma entre {num1} y {num2} es: {num1+num2}")
def restar():
    num1= int(input("Ingrese un número: "))
    num2 = int(input("Ingrese otro número: "))
    print(f"La resta entre {num1} y {num2} es: {num1-num2}")

def multiplicar():
    num1= int(input("Ingrese un número: "))
    num2 = int(input("Ingrese otro número: "))
    if num1 == 0 or num2 == 0:
        print("El resultado es cero.")
    print(f"El producto entre {num1} y {num2} es: {num1*num2}")

def dividir():
    num1= int(input("Ingrese un número: "))
    num2 = int(input("Ingrese otro número: "))
    if num2 == 0:
        print("No se puede dividir por cero")
    print(f"El cociente entre {num1} y {num2} es: {num1/num2}")

def main():
    while True:
        elección = int(input("Ingrese el número correspondiente a la operación.\n(1)Sumar\n(2)Restar\n(3)Multiplicar\n(4)Dividir\n(0)Para salir"))
        if elección == 1:
            sumar()
        elif elección == 2:
            restar()
        elif elección == 3:
            multiplicar()
        elif elección == 4:
            dividir()
        elif elección == 0:
            break
        else:
            continue


if __name__ ==  "__main__":
    main()