def comparar_numeros(num1=0,num2=0):
    #Condicionales que entregan información sobre que número es mayor.
    if num1 > num2:
        print(f"El número {num1} es mayor que {num2}")
    elif num2 > num1:
        print(f"El número {num2} es mayor que {num1}")
    else:
        print("Son iguales")

def main():
    #Variables de ayuda
    son_numeros = False
    numerillo1 = 0
    numerillo2 = 0
    
    #Ciclo while para comprobar que ambos son números
    while son_numeros != True:
        numerote1= input("Ingrese un número: ")
        numerote2 = input("Ingrese otro número: ")

        #Comprueba que ambos datos ingresados sean números (por eso el and y no el or).
        if numerote1.isnumeric() and numerote2.isnumeric():
            numerillo1 = int(numerote1)
            numerillo2 = int(numerote2)
            #Llama a la función que los compara.
            comparar_numeros(num1=numerillo1,num2=numerillo2)
            son_numeros= True
        else:
            print("\t Por favor, solo ingrese números.")

if __name__ == "__main__":
    main()
