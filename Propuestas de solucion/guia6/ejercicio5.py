def capitalizar_nombres(nombre):
    nombres = nombre.split()
    nombres_capitalizados = [n.capitalize() for n in nombres]
    resultado = ""
    for i, n in enumerate(nombres_capitalizados):
        if i == 0:
            resultado = f"{n}"
        else:
            resultado = f"{resultado} {n}"
    return resultado

def main():
    nombre = input("Ingrese un nombre completo: ")
    nombre_capitalizado = capitalizar_nombres(nombre)
    print(f"Nombre capitalizado: {nombre_capitalizado}")

if __name__ == "__main__":
    main()