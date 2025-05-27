#Función que entrega los primos hasta el 100. Se hizo función aparte de la Main() para que se acostumbren a que: Cada acción es una posible función.
def primos():
    num = 2
    while num <= 100:
        es_primo = True
        i = 2
        while i < num:
            if num % i == 0:
                es_primo = False
                break
            i += 1
        if es_primo:
            print(num)
        num += 1


def main():
    primos()

if __name__ == "__main__":
    main()