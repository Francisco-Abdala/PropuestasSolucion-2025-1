def tiene_codon_inicio(secuencia: str):
    # Verificamos que la secuencia tenga al menos 3 caracteres
    if len(secuencia) < 3:
        return False
    
    #Iteramos solo hasta la posición donde aún podemos leer 3 caracteres
    for i in range(len(secuencia) - 2):
        if secuencia[i] == "A" and secuencia[i+1] == "T" and secuencia[i+2] == "G":
            return True
    return False

def codon(verificacion: bool):
    if verificacion:
        print("Existe codón de inicio")
    else:
        print("No existe codón de inicio")

def main():
    secuencia = "AAT"
    resultado = tiene_codon_inicio(secuencia=secuencia)
    codon(resultado)

if __name__ == "__main__":
    main()