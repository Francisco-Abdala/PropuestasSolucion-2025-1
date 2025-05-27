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

#Se usan listas para almacenar números.
def mayor_menor(lista: list):
    #Se inicializan dos variables con el primer número de la lista.
    menor = lista[0]
    mayor = lista[0]
    for numero in lista:
        #Se van comprobando las desigualdades de los números.
        if numero < menor:
            menor = numero
        if numero > mayor:
            mayor = numero
    #Se puede retornar más de un valor.
    return menor, mayor
def main():
    #Se crea la lista para almacenar los números.
    guardar_numeros= []
    print("\t Cuántos números desea ingresar?")
    cantidad = verificar_numero()

    for i in range(cantidad):
        ingreso = verificar_numero()
        guardar_numeros.append(ingreso)
    #Almacena los 2 números retornados por la función.
    primero,ultimo = mayor_menor(guardar_numeros)
    print(f"El número menor de la lista es: {primero} y el mayor es: {ultimo}")


if __name__ == "__main__":
    main()