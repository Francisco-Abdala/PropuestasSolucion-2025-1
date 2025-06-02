import random
def mostrar_informacion(secuencia:str):
    #Función len() calcula la longitud de un texto.
    #El primer caracter corresponde al índice 0.
    #El último caracter corresponde al índice de la longitud-1,esto porque se empieza a contar desde 0.
    print(f"La longitud de la secuencia es: {len(secuencia)}\nLa primera base es: {secuencia[0]}\nLa última base es: {secuencia[len(secuencia)-1]}")

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
    mostrar_informacion(secuencia=secuencia)

if __name__ == "__main__":
    main()