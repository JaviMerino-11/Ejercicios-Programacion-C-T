# Escribe una función que reciba como argumento un número variable de tuplas que
# contengan cada una pares (trabajador, salario), y escriba en la salida estándar la media de los salarios.

# Vamos a crear una funcion que tenga como argumento de entrada un numero cualquiera pero, preferiblemente de tuplas,
# y vamos a ir recorriendo toda la tupla de entrada para quedarnos con los pares de empleado-salario. A continuacion,
# volvemos a iterar este par y almacenamos los salarios (fijamos como condicion que los salarios esten en la segunda
# posicion de la tupla). Al haber almacenado los salarios en una lista, hacemos la suma total de los elementos y
# obtenemos su media.


def calcula_media_salarios(*arg: tuple):
    salarios = []

    for pares_tupla in arg:
        for trabajador_salario in pares_tupla:
            salarios.append(trabajador_salario[1])

    media_salarios = sum(salarios) / len(salarios)

    return media_salarios


def main():
    registro_empleado_salario = (('Jose', 10), ('Gregorio', 10), ('Javi', 15), ('Paco', 30), ('Manuel', 5))

    print("La media de los salarios es %f" % calcula_media_salarios(registro_empleado_salario))


if __name__ == '__main__':
    main()
