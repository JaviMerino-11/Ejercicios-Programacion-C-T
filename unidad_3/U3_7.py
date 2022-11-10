# Escribe una función que tenga sentido, que reciba un número de argumentos posicionales,
# otros opcionales y otros opcionales como diccionario.

# Hacemos un sistema que muestre la informacion de un ciudadano permitiendo la entrada de informacion adicional o no


def mostrar_informacion(pais_residencia: str, comunidad_autonoma: str, *args, **kwargs):
    if kwargs or args:
        print("Pais de residencia: %s\nComunidad autonoma: %s" % (
            pais_residencia, comunidad_autonoma), "\nInformacion adicional: ", kwargs or args)
    else:
        print("Pais de residencia: %s\nComunidad autonoma: %s\nInformacion adicional: No info adicional" % (
            pais_residencia, comunidad_autonoma))


def main():
    nombre_ciudadano = input("Introduzca su nombre: ")
    edad_ciudadano = (input("Introduzca su edad: "))
    pais_residencia = input("Introduzca su pais de residencia: ")
    comunidad_autonoma = input("Introduzca la comunidad autonoma donde vive: ")

    if nombre_ciudadano and edad_ciudadano:
        datos_adicionales = {
            nombre_ciudadano: edad_ciudadano
        }
        mostrar_informacion(pais_residencia=pais_residencia, comunidad_autonoma=comunidad_autonoma,
                            nombre_y_edad=datos_adicionales)
    else:
        mostrar_informacion(pais_residencia=pais_residencia, comunidad_autonoma=comunidad_autonoma)


if __name__ == '__main__':
    main()
