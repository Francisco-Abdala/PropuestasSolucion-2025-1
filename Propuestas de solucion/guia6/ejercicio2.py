def invertir_cadena(cadena):
    cadena_invertida = ""
    for i in range(len(cadena) - 1, -1, -1):
        cadena_invertida += cadena[i]
    return cadena_invertida
def main():
    cadena = input("Ingrese una cadena de texto: ")
    cadena_invertida = invertir_cadena(cadena)
    print(f"La cadena invertida es: {cadena_invertida}")
if __name__ == "__main__":
    main()