def convertir_tiempo(segundos_totales):
    # Calcular horas usando división entera
    horas = segundos_totales // 3600
    
    # Calcular minutos restantes después de extraer las horas
    minutos = (segundos_totales % 3600) // 60
    
    # Calcular segundos restantes
    segundos = segundos_totales % 60
    
    return horas, minutos, segundos

def mostrar_tiempo(segundos_totales):
    horas, minutos, segundos = convertir_tiempo(segundos_totales)
    return f"{horas:02d}:{minutos:02d}:{segundos:02d}"

def main():
    segundos = int(input("Ingrese la cantidad de segundos a calcular: "))
    h, m, s = convertir_tiempo(segundos_totales=segundos)
    print(f"\nResultado: {h} horas, {m} minutos, {s} segundos")
    print(f"Formato: {mostrar_tiempo(segundos_totales=segundos)}")


if __name__ == "__main__":
    main()