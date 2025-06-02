def tablas(num=0):
    for i in range(1,11):
        print(f"El valor de {num} por {i} es igual a: {num*i}")


def main():
    numero = 5
    tablas(num=numero)

if __name__ == "__main__":
    main()