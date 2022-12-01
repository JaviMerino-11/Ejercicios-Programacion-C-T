# Escribe una función que reciba un número variable de parámetros clave y una clave (string) como posicional
# obligatorio y que muestre por la salida estándar el valor asociado a dicha clave, gestionando el caso de que no exista
# ningún valor asociado a dicha clave.


from typing import Dict


# Para ello vamos a crear una funcion que permita sacar el valor asociado a una clave y lance una excepcion en el caso
# en el que esa key no pertenezca al diccionario de entrada.

def mostrar_valor_diccionario(diccionario_entrada: Dict, clave_evaluacion):
    if clave_evaluacion not in diccionario_entrada.keys():
        raise Exception("La clave", clave_evaluacion, "no pertenece al diccionario", diccionario_entrada)
    else:
        print("El valor asociado a la clave", clave_evaluacion, "del diccionario", diccionario_entrada, "es",
              diccionario_entrada[clave_evaluacion])


def main():
    diccionario_entrada = {
        "clave_1": "valor_1",
        "clave_2": "valor_2"
    }
    clave_evaluacion_1 = "clave_1"
    clave_evaluacion_2 = "clave_2"
    clave_evaluacion_3 = "clave_inexistente"

    mostrar_valor_diccionario(diccionario_entrada=diccionario_entrada, clave_evaluacion=clave_evaluacion_1)
    mostrar_valor_diccionario(diccionario_entrada=diccionario_entrada, clave_evaluacion=clave_evaluacion_2)
    mostrar_valor_diccionario(diccionario_entrada=diccionario_entrada, clave_evaluacion=clave_evaluacion_3)


if __name__ == '__main__':
    main()
