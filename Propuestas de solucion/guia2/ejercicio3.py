#Dado que varios ejercicios piden números, se sabe que es una acción que se repite, a lo cual, se crea una función para esto.
def pedir_numero():
    es_numero = False
    numero = 0
    while es_numero != True:
        numerote = input("Ingrese su edad:")
        if numerote.isnumeric():
            numero = int(numerote)
            if numero >=0:
                return numero
        else:
            print("\t Por favor, ingrese un número válido.")

def main():
    #Como pedir_numero() retorna un valor, se le puede entregar este valor a una variable.
    edad = pedir_numero()
    #Al saber que la variable edad siempre es un número, se puede realizar las comparaciones sin ningún miedo.
    if edad > 17:
        print("Eres mayor de edad")
    elif edad < 18:
        print("Eres menor de edad")

if __name__ == "__main__":
    main()