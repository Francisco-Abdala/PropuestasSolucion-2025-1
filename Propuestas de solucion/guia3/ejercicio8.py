def paridad(num=0):
    if num % 2 == 0:
        return True
    else:
        return False
    

def main():
    numero = 1
    if paridad(num=numero):
        print("El número es par.")
    else:
        print("El número no es par.")

if __name__ == "__main__":
    main()