def contar_positivos(secuencia:str):
    contar_total = 0
    contar_K = 0
    contar_H = 0
    contar_R = 0
    for aminoacido in secuencia:
        if aminoacido == "K" or aminoacido == "k":
            contar_total = contar_total +1
            contar_K = contar_K + 1
        elif aminoacido == "R" or aminoacido == "r":
            contar_total = contar_total +1
            contar_R = contar_R + 1
        elif aminoacido == "H" or aminoacido == "h":
            contar_total = contar_total +1
            contar_H = contar_H +1

    return contar_total, contar_H, contar_K , contar_R


def main():
    cadena = "MVKHRRLQKGHPLK"
    cantidad_total, cantidad_h, cantidad_k, cantidad_r=contar_positivos(cadena)
    print(":3")
    if cantidad_total >= 10:
        print(f"La cadena {cadena} es muy positiva\nTiene {cantidad_r} R\nTiene {cantidad_k} K\nTiene {cantidad_h} H")
    else:
        print(f"La cadena {cadena} es muy negativa\nTiene {cantidad_r} R\nTiene {cantidad_k} K\nTiene {cantidad_h} H")

main()