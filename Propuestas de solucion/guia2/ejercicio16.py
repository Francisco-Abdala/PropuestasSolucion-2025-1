def verificar_numero():
    es_numero = False
    numerote = 0
    while es_numero != True:
        palabra = input("Ingrese un número: ")
        if palabra.isnumeric():
            numerote = int(palabra)
            break
        else:
            print("\t Ingrese un número válido.")
    return numerote

#Uso de recursión para calcular Fibonacci.
def fibonacci(num=0):
    if num <= 1:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

def main():
    print("Ingrese hasta que número quiere la secuencia de fibonacci: ")
    numero = verificar_numero()
    fibo = fibonacci(num=numero)
    for i in range(numero):
        print(fibonacci(i)) 

if __name__ == "__main__":
    main()