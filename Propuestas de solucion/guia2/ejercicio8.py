#Entrega la tabla del cinco hasta el número que ingresa el usuario.
def tabla_cinco(num=0):
    for i in range(num+1):
        print(i*5)

#Háganse amigxs de esta función, ayuda al manejo de errores.
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
    tabla_cinco(num=numerillo)


if __name__ == "__main__":
    main()