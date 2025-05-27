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

def generar_combinaciones(numeros:list):
    #Muestra solo los números.
    for i in range(5):
        print(numeros[i])

    #Muestra un número seguido de los demás. El for i .... no avanza hasta que termina el for j... Es por esto que, se muestra el 1,1; 1,2; 1;3 etc.
    for i in range(5):
        for j in range(i + 1, 5):
            print(f"{numeros[i]}, {numeros[j]}")

    #La misma lógica para los demás
    for i in range(5):
        for j in range(i + 1, 5):
            for k in range(j + 1, 5):
                print(f"{numeros[i]}, {numeros[j]}, {numeros[k]}")
    
    for i in range(5):
        for j in range(i + 1, 5):
            for k in range(j + 1, 5):
                for l in range(k + 1, 5):
                    print(f"{numeros[i]}, {numeros[j]}, {numeros[k]}, {numeros[l]}")
    
    print(f"{numeros[0]}, {numeros[1]}, {numeros[2]}, {numeros[3]}, {numeros[4]}")

def main():
    numeros = []
    print("Ingrese 5 números:")
    for _ in range(5):
        usuario = verificar_numero()
        numeros.append(usuario)
    
    print("\tCombinaciones generadas:")
    generar_combinaciones(numeros=numeros)
    
if __name__ == "__main__":
    main()