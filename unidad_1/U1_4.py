# Dadas dos cadenas de caracteres, c1 y c2, escribe código
# para insertar c2 en medio de c1 ('hola', 'adiós' → 'hoadiósla')

# He creado una funcion que recibe dos cadenas de caracteres como argumentos de entrada, como se exige que ambas cadenas
# sean hola y adios y que justo adios este entre ho- y -la, he creado una variable para encontrar la silaba -la, de modo
# que la cadena combinada sera ho hasta la posicion donde se encuentra la, + la cadena 2 entera seguida por la.
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
