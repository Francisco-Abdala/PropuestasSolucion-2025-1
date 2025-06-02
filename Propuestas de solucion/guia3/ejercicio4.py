def traducir(codon:str):
    #Condicionales con todas las posibles conformaciones que puede tener un codón.
    if codon.upper() == "AUG":
        print(f"El codón {codon} corresponde al aminoácido Metionina")

    elif codon.upper() == "UUU" or codon.upper() == "UUC":
        print(f"El codón {codon} corresponde al aminoácido Fenilalanina")

    elif codon.upper() == "UUA" or codon.upper() == "UUG" or codon.upper() == "CUU" or codon.upper() == "CUC" or codon.upper() == "CUA" or codon.upper() == "CUG":
        print(f"El codón {codon} corresponde al aminoácido Leucina")

    elif codon.upper() == "AUU" or codon.upper() == "AUC" or codon.upper() == "AUA":
        print(f"El codón {codon} corresponde al aminoácido Isoleucina")

    elif codon.upper() == "GUU" or codon.upper() == "GUC" or codon.upper() == "GUA" or codon.upper() == "GUG":
        print(f"El codón {codon} corresponde al aminoácido Valina")

    elif codon.upper() == "UCU" or codon.upper() == "UCC" or codon.upper() == "UCA" or codon.upper() == "UCG" or codon.upper() == "AGU" or codon.upper() == "AGC":
        print(f"El codón {codon} corresponde al aminoácido Serina")

    elif codon.upper() == "CCU" or codon.upper() == "CCC" or codon.upper() == "CCA" or codon.upper() == "CCG":
        print(f"El codón {codon} corresponde al aminoácido Prolina")

    elif codon.upper() == "ACU" or codon.upper() == "ACC" or codon.upper() == "ACA" or codon.upper() == "ACG":
        print(f"El codón {codon} corresponde al aminoácido Treonina")

    elif codon.upper() == "GCU" or codon.upper() == "GCC" or codon.upper() == "GCA" or codon.upper() == "GCG":
        print(f"El codón {codon} corresponde al aminoácido Alanina")

    elif codon.upper() == "UAU" or codon.upper() == "UAC":
        print(f"El codón {codon} corresponde al aminoácido Tirosina")
    
    elif codon.upper() == "UAA" or codon.upper() == "UAG" or codon.upper() == "UGA":
        print(f"El codón {codon} corresponde a un Stop")

    elif codon.upper() == "CAU" or codon.upper() == "CAC":
        print(f"El codón {codon} corresponde al aminoácido Histidina")
    
    elif codon.upper() == "CAA" or codon.upper() == "CAG":
        print(f"El codón {codon} corresponde al aminoácido Glutamina")

    elif codon.upper() == "AAU" or codon.upper() == "AAC":
        print(f"El codón {codon} corresponde al aminoácido Asparagina")

    elif codon.upper() == "AAG" or codon.upper() == "AAG":
        print(f"El codón {codon} corresponde al aminoácido Lisina")
    
    elif codon.upper() == "GAU" or codon.upper() == "GAC":
        print(f"El codón {codon} corresponde al aminoácido Aspartato")

    elif codon.upper() == "GAA" or codon.upper() == "GAG":
        print(f"El codón {codon} corresponde al aminoácido Glutamato")

    elif codon.upper() == "CGU" or codon.upper() == "CGC" or codon.upper() == "CGA" or codon.upper() == "CGG" or codon.upper() == "AGA" or codon.upper() == "AGG" :
        print(f"El codón {codon} corresponde al aminoácido Arginina")

    elif codon.upper() == "GGU" or codon.upper() == "GGC" or codon.upper() == "GGA" or codon.upper() == "GGG":
        print(f"El codón {codon} corresponde al aminoácido Glicina")
    
    elif codon.upper() == "UGU" or codon.upper() == "UGC":
        print(f"El codón {codon} corresponde al aminoácido Cisteína")
    else:
        print("No se ha ingresado un codón.")
    
def pedir_codon():
    #Verifica que lo ingresado sea de la longitud de un codón.
    while True:
        codon = input("Ingrese su codón: ")
        if len(codon) == 3:
            break
        else:
            continue
    return codon

def main():
    codon = pedir_codon()
    traducir(codon=codon)

if __name__ == "__main__":
    main()