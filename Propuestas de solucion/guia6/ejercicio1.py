def contar_vocales(texto:str):
    conteo = 0
    for letra in texto:
        if letra.lower() == "a" or letra.lower() == "e" or letra.lower() == "i" or letra.lower() =="o" or letra.lower() == "u":
            conteo = conteo + 1
    return conteo

def main():
    palabra = "murcielago"
    vocales = contar_vocales(palabra)
    print(vocales)

if __name__ == "__main__":
    main()
