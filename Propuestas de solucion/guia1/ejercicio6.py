def primo(limite=0):
    #Recorre todos los números desde cero hasta el valor ingresado por el usuario.
    for num in range(limite):

        #Se crea una variable que entregará información respecto a si es o no primo.
        es_primo = True

        #Cero y uno no son primos.
        if num == 0 or num == 1:
            es_primo = False

        #Se calculan los primos.
        for i in range(2,int(num ** 0.5)+1):
            if num %i == 0:
                es_primo = False
                break
        if es_primo:
            print(num)


def main():
    while True:
        #Se pide ingresar un número positivo
        limite = int(input("Ingrese un número entero positivo"))

        #Si es negativo, que continúe el ciclo.
        if limite < 0:
            continue
        else:
            #Realiza la función si es un número positivo.
            primo(limite=limite)
            break

if __name__ == "__main__":
    main()