def validacion_numero(numero=0):
    #Condiciones encargadas de entregar la información del número.
    if numero > 0:
        print("El número ingresado es positivo.")
    elif numero < 0:
        print("El número ingresado es negativo.")
    else:
        print("El número ingresado es cero.")

def main():
    #Variables de ayuda
    es_numero = False
    numero = 0
    #Ciclo while para corroborar que lo ingresado siempre sea un número.
    while es_numero != True:
        numerito = input("Ingrese un número")
        #Valida que sea un número, si lo es, ejecuta la función validacion_numero(). Si no es, continua pidiendo un número.
        if numerito.isnumeric():
            numero = int(numerito)
            validacion_numero(numero=numero)
            es_numero = True
        else:
            continue

if __name__ == "__main__":
    main()