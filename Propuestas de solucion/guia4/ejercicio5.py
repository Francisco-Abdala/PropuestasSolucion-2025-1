def calcular_promedio(num1=0,num2=0,num3=0):
    return (num1 + num2 + num3) / 3

def main():
    print("Calculadora de promedio de tres números")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))
    
    promedio = calcular_promedio(num1, num2, num3)
    print(f"El promedio de los números es: {promedio}")

if __name__ == "__main__":
    main()