def analizar_longitud(texto):
    longitud = len(texto)
    primera_letra = texto[0]
    ultima_letra = texto[-1]
    return longitud, primera_letra, ultima_letra

def main():
    texto = input("Ingrese un texto: ")
    longitud, primera_letra, ultima_letra = analizar_longitud(texto)
    print(f"Longitud del texto: {longitud}")
    print(f"Primera letra: {primera_letra}")
    print(f"Última letra: {ultima_letra}")
if __name__ == "__main__":
    main()