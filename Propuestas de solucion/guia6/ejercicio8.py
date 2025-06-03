def eliminar_espacios(texto):
    return texto.replace(" ", "")

def main():
    texto = input("Ingrese un texto: ")
    texto_sin_espacios = eliminar_espacios(texto)
    print(f"Texto sin espacios: {texto_sin_espacios}") 

if __name__ == "__main__":
    main()