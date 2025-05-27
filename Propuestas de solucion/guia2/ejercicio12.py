#Importa la librería Random.
import random
def numero_random():
    return random.randint(1,100) #Entrega un valor aleatorio en el rango 1-100.

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
    aleatorio = numero_random()
    #Esta vez, sin variables de ayuda para entender el funcionamiento de la palabra "break".
    while True:
        #Se ingresa un número
        usuario = verificar_numero()
        #Comprueba las opciones de: si el valor ingresado es mayor o menor.
        if aleatorio > usuario:
            print(f"El número {usuario} es demasiado bajo")
        elif usuario > aleatorio:
            print(f"El nímero {usuario} es demasiado alto")
        else:
            #En caso de que no cumpla ninguna de esas condiciones, significa que el número ingresado es el correcto.
            print("Adivinaste")
            break #A lo cual, "break" rompe el ciclo, es lo mismo a que una variable ayuda tuviera el valor de False.

if __name__ == "__main__":
    main()