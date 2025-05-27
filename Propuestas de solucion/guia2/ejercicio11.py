#Función que verifica que el número ingresado sea primo.
def es_primo(num=0):
    #Si es 0,1 o divisible por 2, se sabe que no es primo.
    if num <= 1:
        return False
    #El dos es el primer primo.
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    

    #Variable de ayuda.
    i = 3

    #Se busca algún otro divisor del número ingresado, para demostrar que NO es primo.
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True


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


def main():
    numerillo = verificar_numero()
    #Como la función es_primo() retorna un booleano (Verdadero o Falso), se puede ocupar directamente en las condicionales.
    if es_primo(numerillo):
        print(f"{numerillo} es primo")
    else:
        print(f"{numerillo} no es primo.")


if __name__ == "__main__":
    main()