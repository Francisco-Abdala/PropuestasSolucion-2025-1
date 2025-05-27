#Tal como se comenta en el ejercicio 5, lo que aparece en la función calcular_promedio() es el tipo de dato.
def calcular_promedio(num: list):
    promedio = 0
    #Recorre los elementos de la lista.
    for numero in range(len(num)):
        promedio = promedio +  (num[numero]/len(num)) #num[numero] se refiere a: tomar el valor que está en el índice "numero" de la lista "num."
    return promedio

#Se crea la función que verifica que lo ingresado sea un número.
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
    #Se crea la lista para almacenar los números.
    numeros = []
    ingreso_num = True # Variable que controla el ciclo while.

    while ingreso_num != False:
        numerillo = verificar_numero()
        #Se agrega el numero ingresado con la función append(), es propia de Python aplicable SOLO a listas.
        numeros.append(numerillo)
        verificar = input("Desea ingresar otro número? Y/n")
        if verificar.upper() == "N":
            ingreso_num = False
    promedio = calcular_promedio(numeros)
    print(f"El promedio de números ingresados es: {promedio}")



if __name__ == "__main__":
    main()