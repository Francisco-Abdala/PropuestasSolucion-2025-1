#Al no tener un return, esto es un procedimiento que muestra los pares en el rango 0-50
def numeros_par():
    for i in range(51):
        if i % 2 == 0:
            print(f"El número {i} es par")

def main():
    #Se llama al procedimiento.
    numeros_par()
    
if __name__ == "__main__":
    main()