def cinco_caracter():
    #Variable de ayuda.
    fin = False
    while fin != True:
        palabrota = input("Ingrese la palabra para determinar su longitud: ")
        contador = 0
        #Se recorre el texto ingresado y se cuenta cuantas letras posee.
        for _ in palabrota:
            contador = contador + 1
        #Si la cantidad de letras es mayor a 5, se cumple la condición.
        if contador >= 5:
            print(f"La palabra {palabrota} tiene más de cinco caracteres.\nLa palabra tiene {contador} caracteres.")
        else:
            print("Tiene menos de cinco caracteres.")
        #Se pide otra palabra .
        confirmacion = input("Desea comprobar otra palabra? Y/n ")
        if confirmacion.lower() == "n":
            fin = True

def main():
    cinco_caracter()

if __name__ == "__main__":
    main()