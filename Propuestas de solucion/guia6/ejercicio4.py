def buscar_subcadena(texto, subcadena):
    if subcadena in texto:
        return True
    else:  
        return False
def main():
    texto = input("Ingrese el texto: ")
    subcadena = input("Ingrese la subcadena a buscar: ")
    if buscar_subcadena(texto, subcadena):
        print(f"La subcadena '{subcadena}' se encuentra en el texto.")
    else:
        print(f"La subcadena '{subcadena}' no se encuentra en el texto.")
if __name__ == "__main__":
    main()