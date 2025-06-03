def normalizar(texto:str):
    nuevo_texto = ""
    for letra in texto:
        if letra == " " or letra == "." or letra == ",":
            continue
        else:
            nuevo_texto = nuevo_texto + letra.lower()
    return nuevo_texto


def main():
    texto = "Hol A mUndO"
    nuevo_texto = normalizar(texto)
    print(texto)
    print(nuevo_texto)

if __name__ == "__main__":
    main()
