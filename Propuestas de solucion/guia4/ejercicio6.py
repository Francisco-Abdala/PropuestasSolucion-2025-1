def contar_bases(secuencia:str):
    contador_A = 0
    contador_T = 0
    contador_G = 0
    contador_C = 0
    for i in secuencia:
        if i == "A":
            contador_A += 1
        elif i == "T":
            contador_T += 1
        elif i == "G":
            contador_G += 1
        elif i == "C":
            contador_C += 1
    return contador_A, contador_T, contador_G, contador_C


def mostrar_contador(contador_A, contador_T, contador_G, contador_C):
    print(f"Cantidad de A: {contador_A}")
    print(f"Cantidad de T: {contador_T}")
    print(f"Cantidad de G: {contador_G}")
    print(f"Cantidad de C: {contador_C}")
def main():
    secuencia = "ATGCGATACGCTAGCTAGCTAGCTAGCTAGC"
    contador_A, contador_T, contador_G, contador_C = contar_bases(secuencia=secuencia)
    mostrar_contador(contador_A, contador_T, contador_G, contador_C)
if __name__ == "__main__":
    main()