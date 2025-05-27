def invertir_cadena(palabra: str):
    #Se crea una variable que almacenará el texto invertido.
    palabra_invertida = ""
    for i in range(1,len(palabra)+1):
        #Concatenación del texto.
        palabra_invertida = palabra_invertida + palabra[-i] #Uso de índices negativos. (Solo funciona en Python).
    print(palabra_invertida)


def main():
    palabrilla = input("Ingrese la palabra a invertir: ")
    invertir_cadena(palabra=palabrilla)

if __name__ == "__main__":
    main()