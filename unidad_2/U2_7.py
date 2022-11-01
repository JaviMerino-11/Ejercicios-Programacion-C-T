# Escribe un guión para almacenar un
# diccionario con los nombres de las facultades de la
# UGR como claves y como valor, otro diccionario con
# los nombres de departamentos como clave y las
# plantas donde se ubican como valor. Recorre y
# muestra por la salida estándar toodo el contenido de dicho diccionario.

# Para ello, vamos a pedirle al usuario que introduzca nombres de facultades, de forma que estas se van almacenar en
# parejas clave-valor -- facultad1:facultad1. Por otro lado, vamos a pedirle tambien nombres de departamentos que se
# almacenaran como claves y la planta donde se ubica como valor. Tras esto, mostraremos por pantalla el contenido de
#

def main():
    nombre_facultad = input("Introduzca el nombre de la facultad: ")
    nombre_dpto = input("Introduzca el nombre del departamento: ")
    numero_planta = input("Introduzca la planta donde se ubica ese departamento: ")

    informacion_facultad = {
        nombre_facultad: nombre_facultad
    }

    informacion_dpto_planta = {
        nombre_dpto: numero_planta
    }

    for departamento, planta in informacion_dpto_planta.items():
        print("Facultad: %s\nDepartamento: %s\nPlanta: %s" % (
            informacion_facultad.get(nombre_facultad), departamento, planta))


if __name__ == '__main__':
    main()
