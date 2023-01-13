# Ejercicio de hilos: Crear un vector de 10 000 muestras de numeros enteros aleatorios.
# Usando 4 hilos, buscar el maximo de ese vector y comparar el valor obtenido por cada uno de los hilos
# y sacar el resultado final

from threading import Thread
import numpy as np

# Declaro una variable global para que todos los hilos accedan a la misma estructura de datos.
VECTOR_NUMEROS_ALEATORIOS_1 = [numero for numero in range(25000)]
VECTOR_NUMEROS_ALEATORIOS_2 = [numero for numero in range(50000)]
VECTOR_NUMEROS_ALEATORIOS_3 = [numero for numero in range(75000)]
VECTOR_NUMEROS_ALEATORIOS_4 = [numero for numero in range(100000)]


# Creo una clase que me permita customizar lo que quiero que haga el propio hilo, de forma que, a la hora de
# inicializarse este, tenga un valor de None y cuando se ejecute el hilo, este devuelva el valor del maximo del
# array de numeros aleatorios de entrada.

class CustomThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.value_1 = None
        self.value_2 = None
        self.value_3 = None
        self.value_4 = None

    def run(self):
        self.value_1 = np.max(VECTOR_NUMEROS_ALEATORIOS_1)
        self.value_2 = np.max(VECTOR_NUMEROS_ALEATORIOS_2)
        self.value_3 = np.max(VECTOR_NUMEROS_ALEATORIOS_3)
        self.value_4 = np.max(VECTOR_NUMEROS_ALEATORIOS_4)


def main():
    # Creamos cada uno de los 4 hilos como instancias de la clase anterior
    hilo_1 = CustomThread()
    hilo_2 = CustomThread()
    hilo_3 = CustomThread()
    hilo_4 = CustomThread()

    # Ejecutamos cada hilo de forma paralela
    hilo_1.start()
    hilo_2.start()
    hilo_3.start()
    hilo_4.start()

    # Esperamos a cada hilo a que termine
    hilo_1.join()
    hilo_2.join()
    hilo_3.join()
    hilo_4.join()

    # Accedemos a cada valor devuelto y lo almacenamos en variables asociadas a cada hilo
    maximo_hilo_1 = hilo_1.value_1
    maximo_hilo_2 = hilo_2.value_2
    maximo_hilo_3 = hilo_3.value_3
    maximo_hilo_4 = hilo_4.value_4

    # Ahora creo una lista con todos los maximos obtenidos y la pinto:
    lista_maximos_obtenidos = [maximo_hilo_1, maximo_hilo_2, maximo_hilo_3, maximo_hilo_4]
    print("La lista de maximos obtenidos de cada ejecución paralela es: " + lista_maximos_obtenidos.__str__())

    # Una vez he mostrado los maximos que he obtenido, voy a quedarme con el maximo de ellos y lo voy a mostrar por
    # pantalla
    maximo_absoluto = max(lista_maximos_obtenidos)
    print("El maximo de todos los valores es: %i" % maximo_absoluto)


if __name__ == '__main__':
    main()
