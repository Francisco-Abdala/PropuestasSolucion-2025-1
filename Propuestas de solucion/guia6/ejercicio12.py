def mutar_adn(secuencia):
    secuencia_mutada = ""
    for base in secuencia:
        if base == 'A':
            secuencia_mutada += 'X'
        else:
            secuencia_mutada += base
    return secuencia_mutada
def main():
    adn = input("Ingrese la secuencia de ADN: ").upper()
    adn_mutado = mutar_adn(adn)
    print(f"Secuencia original: {adn}")
    print(f"Secuencia mutada: {adn_mutado}")
if __name__ == "__main__":
    main()