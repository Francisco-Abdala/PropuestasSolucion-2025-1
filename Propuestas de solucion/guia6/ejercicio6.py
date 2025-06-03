def contar_palabra(texto, palabra):

    # Convertir el texto y la palabra a minúsculas para una comparación insensible a mayúsculas
    texto = texto.lower()
    palabra = palabra.lower()
    
    # Dividir el texto en palabras y contar las ocurrencias de la palabra
    palabras = texto.split()
    return palabras.count(palabra)
def main():
    texto = input("Ingrese el texto: ")
    palabra = input("Ingrese la palabra a contar: ")
    
    cantidad = contar_palabra(texto, palabra)
    
    print(f"La palabra '{palabra}' aparece {cantidad} veces en el texto.")
if __name__ == "__main__":
    main()