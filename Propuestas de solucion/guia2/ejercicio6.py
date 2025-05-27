#Función que calcula la suma hasta cierto número.
def calcular_suma(num=0):
    min = 1
    suma = 0
    while min <= num:
        #Se guarda las sumas de un número a otro.
        suma = suma + min
        #Se va aumentando el número hasta que llegue al número pedido.
        min = min + 1
    return suma

def main():
    #Variables de ayuda.
    es_numero = False
    numerillo = 0
    #Comprueba que lo ingresado sea siempre un número.
    while es_numero != True:
        numero =  input("Ingrese un número: ")
        if numero.isnumeric():
            numerillo = int(numero)
            #Se llama a la función.
            total = calcular_suma(num=numerillo)
            print(f"La suma desde 1 hasta {numerillo} es {total}")
            break
        else:
            print("\t Ingrese un número válido")

if __name__ == "__main__":
    main()