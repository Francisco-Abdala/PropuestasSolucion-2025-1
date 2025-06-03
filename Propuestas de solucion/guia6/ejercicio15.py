def resumen(texto:str):
    print(f"Texto: {texto}\nLargo: {len(texto)}\nMayúsculas: {texto.upper()}\nMinúsculas: {texto.lower()}")

def main():
    texto = "dmfksmfka"
    resumen(texto=texto)

if __name__ == "__main__":
    main()