def contar_frecuencia_letras():
    texto = input("Ingrese una palabra:").lower()
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    #Se crea una lista para almacenar la frecuencia de cada letra. Por ejemplo, el índice 0 corresponde a la A, índice 1 a la B, etc.
    frecuencia = [0] * len(alfabeto)
    
    #Cuenta la frecuencia de cada letra.
    for caracter in texto:
        #Verificar si el caracter está en el alfabeto.
        for i in range(len(alfabeto)):
            #Si el caracter está en la posición i del alfabeto, suma uno en el índice de frecuencias.
            if caracter == alfabeto[i]:
                frecuencia[i] += 1
                break
    #Recorre los 27 elementos de la lista frecuencia.
    for i in range(len(alfabeto)):
        #Condición para mostrar frecuencias de letras ingresadas. 
        if frecuencia[i] > 0:
            if frecuencia[i] == 1:
                print(f"La letra '{alfabeto[i]}' aparece {frecuencia[i]} vez")
            else:
                print(f"La letra '{alfabeto[i]}' aparece {frecuencia[i]} veces")
    


def main():
    contar_frecuencia_letras()


if __name__ == "__main__":
    main()