# Dadas dos cadenas de caracteres, c1 y c2, escribe código
# para insertar c2 en medio de c1 ('hola', 'adiós' → 'hoadiósla')

def combinar_cadenas_mitad(cadena_1: str, cadena_2: str):
    index = cadena_1.find('la')
    cadena_1_combinada = cadena_1[:index] + cadena_2 + cadena_1[index:]
    print("Se ha obtenido %s tras combinar %s en la mitad de %s." % (cadena_1_combinada, cadena_2, cadena_1))


def main():
    cadena_1 = "hola"
    cadena_2 = "adiós"

    combinar_cadenas_mitad(cadena_1=cadena_1, cadena_2=cadena_2)


if __name__ == '__main__':
    main()
