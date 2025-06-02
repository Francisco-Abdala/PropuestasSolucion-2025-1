import random
def crear_secuencia():
    #Se inician la variable secuencia vacía para concatenar luego.
    secuencia = ""
    #Se crea una lista con las bases nitrogenadas.
    BASES = ["A","T","C","G","n"]
    #Se crean secuencia de largo 20.
    for _ in range(20):
        #Genera un número aleatorio entre 0-4.
        ayuda = random.randint(0,4)
        #Se concatena la cadena.
        secuencia = secuencia + BASES[ayuda]
    #Se retorna la secuencia creada.
    return secuencia

def conteo_bases(secuencia: str):
    #Se inicializan las variables para contar caracteres.
    conteo_A= 0
    conteo_T= 0
    conteo_C= 0
    conteo_G= 0
    conteo_nulo = 0
    #Se recorre la secuencia a analizar.
    for base in secuencia:
        #Las condiciones para aumentar el valor de las variables.
        if base.upper() == "A":
            conteo_A = conteo_A + 1
        elif base.upper() == "T":
            conteo_T = conteo_T + 1
        elif base.upper() == "C":
            conteo_C = conteo_C + 1
        elif base.upper() == "G":
            conteo_G = conteo_G + 1
        else:
            conteo_nulo = conteo_nulo + 1
    #Si la cantidad de letras válidas es la misma que la secuencia, es porque no existen caracteres no válidos.
    if conteo_A + conteo_C + conteo_T + conteo_G == len(secuencia):
        return True
    else:
        return False
        
def main():
    secuencia = crear_secuencia()
    if conteo_bases(secuencia=secuencia):
        print("La secuencia es válida")
    else:
        print("La secuencia no es válida")

if __name__ == "__main__":
    main()