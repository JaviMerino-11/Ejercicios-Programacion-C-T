# Escribe una función que reciba dos parámetros enteros
# y gestione correctamente la división por cero y que alguno o los
# dos no sean enteros o reales.

# Para ello vamos a crear una funcion que reciba dos parametros que han de ser numeros enteros,
# y vamos a discriminar entre dos casos para lanzar excepciones: dividir por 0 o que alguno de los parametros de entrada
# no sea ni enteros ni reales. Vamos a suponer que siempre vamos a dividir numero_1 / numero_2 -- Por lo que numero_2
# no puede ser 0

def division_numeros_enteros(numero_1: int, numero_2: int):
    if type(numero_1) == int and type(numero_1) == int and numero_2 != 0:
        print("El resultado de la división es:", numero_1 / numero_2)
    elif type(numero_1) == complex or type(numero_2) == complex:
        raise Exception("No se toleran numeros complejos, introduzca numeros enteros.")
    elif numero_2 == 0:
        raise Exception(
            "El denominador no puede ser 0. Cambie el segundo numero de entrada por uno entero distinto de 0.")


def main():
    numero_1 = int(input("Introduzca el numero del numerador: "))
    numero_2 = int(input("Introduzca el numero del denominador: "))

    division_numeros_enteros(numero_1=numero_1, numero_2=numero_2)


if __name__ == '__main__':
    main()
