def es_adn_valido(secuencia:str):
    for letra in secuencia:
        if letra not in "ATCG":
            return False
    return True


def resultado(validacion:bool):
    if validacion:
        print("La secuencia de ADN es válida.")
    else:
        print("La secuencia de ADN no es válida.")
def main():
    secuencia = input("Introduce la secuencia de ADN: ")
    validacion = es_adn_valido(secuencia)
    resultado(validacion)
if __name__ == "__main__":
    main()