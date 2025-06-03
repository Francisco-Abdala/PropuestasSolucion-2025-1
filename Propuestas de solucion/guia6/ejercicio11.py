def contar_bases(adn):
    contar_a=0
    contar_t=0
    contar_c=0
    contar_g=0
    
    for base in adn:
        if base == 'A':
            contar_a += 1
        elif base == 'T':
            contar_t += 1
        elif base == 'C':
            contar_c += 1
        elif base == 'G':
            contar_g += 1
    return contar_a, contar_t, contar_c, contar_g
def main():
    adn = input("Ingrese la secuencia de ADN: ").upper()
    contar_a, contar_t, contar_c, contar_g = contar_bases(adn)
    
    print(f"Cantidad de A: {contar_a}")
    print(f"Cantidad de T: {contar_t}")
    print(f"Cantidad de C: {contar_c}")
    print(f"Cantidad de G: {contar_g}")
if __name__ == "__main__":
    main()