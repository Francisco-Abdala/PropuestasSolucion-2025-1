def reemplazar_letras(texto, letra_a_reemplazar, letra_reemplazo):
    return texto.replace(letra_a_reemplazar, letra_reemplazo)


def main(): 
    texto = input("Ingrese un texto: ")
    letra_a_reemplazar = input("Ingrese la letra a reemplazar: ")
    letra_reemplazo = input("Ingrese la letra de reemplazo: ")

    texto_modificado = reemplazar_letras(texto, letra_a_reemplazar, letra_reemplazo)
    print(f"Texto modificado: {texto_modificado}")
if __name__ == "__main__":
    main()