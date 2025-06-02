import random
def informacion(secuencia: str,nombre:str):
    #Se inicializan las variables para contar caracteres.
    cantidadGC = 0
    #Se recorre la secuencia a analizar.
    for base in secuencia:
        #Las condiciones para aumentar el valor de las variables.
        if base.upper() == "C" or base.upper() == "G":
            cantidadGC = cantidadGC + 1 
    #Se calcula el porcentaje G-C.
    porcentajeGC = (cantidadGC/len(secuencia))* 100

    print(f"El nombre de la secuencia es: {nombre}\nLa secuencia es: {secuencia}\nEl porcentaje G-C de la secuencia es: {porcentajeGC}%\nLa longitud de la secuencia es de: {len(secuencia)}") 


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
    nombre = input("Ingrese el nombre de su secuencia aleatoria: ")
    secuencia = crear_secuencia()
    informacion(secuencia=secuencia,nombre=nombre)

if __name__ == "__main__":
    main()