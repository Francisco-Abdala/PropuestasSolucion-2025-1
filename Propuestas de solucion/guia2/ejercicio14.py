#Se reutiliza la función de invertir cadenas de texto. 
def invertir_cadena(palabra: str):
    palabra_invertida = ""
    for i in range(1,len(palabra)+1):
        palabra_invertida = palabra_invertida + palabra[-i]
    return palabra_invertida
def main():
    palabrita = input("Ingrese una palabra para confirmar, o no, que es palndromica: ")
    palabrota = invertir_cadena(palabra=palabrita)
    #Se comprueba directamente si las palabras son iguales. Esto se podría hacer letra a letra.
    if palabrita.lower() == palabrota.lower():
        print("Es palindromo")
    else:
        print("No son palindromos")

if __name__ == "__main__":
    main()