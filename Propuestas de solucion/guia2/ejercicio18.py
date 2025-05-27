def crear_triangulo(filas = 0):
    triangulo = []
    for i in range(filas):
        fila = [1] 
        if i > 0:
            for j in range(1, i):
                valor = triangulo[i - 1][j - 1] + triangulo[i - 1][j]
                fila.append(valor)
            fila.append(1)
        triangulo.append(fila)
    return triangulo

def ver_triangulo(triangulo:list):
    ultima_fila = triangulo[-1]
    texto_ultima = ""
    for numero in ultima_fila:
        texto_ultima += str(numero) + " "

    ancho_maximo = len(texto_ultima)
    for fila in triangulo:
        texto_fila = ""
        for numero in fila:
            texto_fila += str(numero) + " "
        largo_fila = len(texto_fila)
        espacios = (ancho_maximo - largo_fila) // 2
        print(" " * espacios + texto_fila)

def verificar_numero():
    es_numero = False
    numerote = 0
    while es_numero != True:
        palabra = input("Ingrese un número: ")
        if palabra.isnumeric():
            numerote = int(palabra)
            break
        else:
            print("\t Ingrese un número válido.")
    return numerote

def main():
    print("Ingrese la cantidad de filas que quiere generar del triángulo de Pascal: ")
    numero = verificar_numero()
    triangulillo = crear_triangulo(numero)
    ver_triangulo(triangulo=triangulillo)


if __name__ == "__main__":
    main()
