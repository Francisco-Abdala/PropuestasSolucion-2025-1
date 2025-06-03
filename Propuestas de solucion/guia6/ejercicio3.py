def es_adn_valido(adn):
    #Divisible en 3 dado que representa codones
    if len(adn) % 3 != 0:
        return False
    for base in adn:
        if base not in ['A', 'T', 'C', 'G']:
            return False
    return True

def main():
    adn = input("Ingrese una cadena de ADN: ").upper()
    if es_adn_valido(adn):
        print("La cadena de ADN es válida.")
    else:
        print("La cadena de ADN no es válida.")
if __name__ == "__main__":  
    main()