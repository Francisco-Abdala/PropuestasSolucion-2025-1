def transcribir_adn(secuencia:str):
    secuencia_nueva = ""
    for letra in secuencia:
        if letra == "T":
            secuencia_nueva = secuencia_nueva + "U"
        else:
            secuencia_nueva = secuencia_nueva + letra
    return secuencia_nueva

def main():
    secuencia = input("Introduce la secuencia de ADN: ")
    secuencia_transcrita = transcribir_adn(secuencia)
    print("Secuencia transcrita a ARN:", secuencia_transcrita)
if __name__ == "__main__":
    main()