import random #Se importa la librería random para generar números aleatorios.

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
    #Se retornan los valores para su posterior uso.
    return conteo_A,conteo_T,conteo_C,conteo_G,conteo_nulo

def crear_secuencia():
    #Se inician la variable secuencia vacía para concatenar luego.
    secuencia = ""
    #Se crea una lista con las bases nitrogenadas.
    BASES = ["A","T","C","G"]
    #Se crean secuencia de largo 20.
    for _ in range(20):
        #Genera un número aleatorio entre 0-3.
        ayuda = random.randint(0,3)
        #Se concatena la cadena.
        secuencia = secuencia + BASES[ayuda]
    #Se retorna la secuencia creada.
    return secuencia

def main():
    secuencia = crear_secuencia()
    print(f"Se desea contar las bases de la siguinte secuencia: {secuencia}")
    cantidadA,cantidadT,cantidadC,cantidadG,cantidadN = conteo_bases(secuencia=secuencia)
    print(f"La cantidad de Adenina es: {cantidadA}\nLa cantidad de Timina es: {cantidadT}\nLa cantidad de Citosina es: {cantidadC}\nLa cantidad de Guanina es: {cantidadG}\nLa cantidad de caracteres no pertenecientes a bases es: {cantidadN}")

if __name__ == "__main__":
    main()