def es_palindromo(palabra):
    palabra = palabra.lower()
    return palabra == palabra[::-1]

def main():
    palabra = input("Ingrese una palabra: ")
    if es_palindromo(palabra):
        print(f"La palabra '{palabra}' es un palíndromo.")
    else:
        print(f"La palabra '{palabra}' no es un palíndromo.")
if __name__ == "__main__":
    main()