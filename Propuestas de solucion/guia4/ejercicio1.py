def contar_positivos(secuencia:str):
    contador_k = 0
    contador_r = 0
    contador_h = 0
    for letra in secuencia:
        if letra == "K":
            contador_k += 1
        elif letra == "R":
            contador_r += 1
        elif letra == "H":
            contador_h += 1
    return contador_k, contador_r, contador_h

def cargada(num1=0, num2=0,num3=0):
    if num1+num2+num3 > 10:
        return True
    else:
        return False
def main():
    secuencia = "MVKHRRLQKGHPLK"    
    contador_k, contador_r, contador_h = contar_positivos(secuencia)
    verificacion = cargada(contador_k, contador_r, contador_h)
    if verificacion:
        print("La secuencia está cargada.")
    else:
        print("La secuencia no está cargada.")
if __name__ == "__main__":
    main()