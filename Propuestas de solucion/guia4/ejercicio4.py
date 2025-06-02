def clasificar_gen(longitud =0):
    if longitud < 100:
        print("Corto")
    if 100 <=longitud <= 1000:
        print("Medio")
    if longitud > 1000:
        print("Largo")
def main():
    secuencia_gen = "ATGCGTACGTAGCTAGCTAGCTAGCTAGCATCGATCGATCGATCGTTAGC"
    clasificar_gen(len(secuencia_gen))
if __name__ == "__main__":
    main()