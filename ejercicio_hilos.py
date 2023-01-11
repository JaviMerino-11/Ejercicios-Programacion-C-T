# Ejercicio de hilos: Crear un vector de 10 000 muestras de numeros enteros aleatorios.
# Usando 4 hilos, buscar el maximo de ese vector y comparar el valor obtenido por cada uno de los hilos
# y sacar el resultado final

from threading import Thread
import numpy as np

# Declaro una variable global para que todos los hilos accedan a la misma estructura de datos.
VECTOR_NUMEROS_ALEATORIOS = np.random.randint(1, 50000, 10000)


# Creo una clase que me permita customizar lo que quiero que haga el propio hilo, de forma que, a la hora de
# inicializarse este, tenga un valor de None y cuando se ejecute el hilo, este devuelva el valor del maximo del
# array de numeros aleatorios de entrada.

class CustomThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.value = None

    def run(self):
        self.value = np.max(VECTOR_NUMEROS_ALEATORIOS)


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
    maximo_hilo_1 = hilo_1.value
    maximo_hilo_2 = hilo_2.value
    maximo_hilo_3 = hilo_3.value
    maximo_hilo_4 = hilo_4.value

    # Creo un set con los maximos obtenidos, de forma que si la longitud de esta estructura es 1, significa que todos
    # los maximos son iguales y, por lo tanto, todos los hilos han llegado a la misma conclusion.
    set_maximos_obtenidos = {maximo_hilo_1, maximo_hilo_2, maximo_hilo_3, maximo_hilo_4}
    if len(set_maximos_obtenidos) == 1:
        print(
            "Los hilos han encontrado el mismo maximo en su ejecucion paralela: " + set_maximos_obtenidos.__str__())
    else:
        print(
            "Los hilos no han encontrado el mismo maximo en su ejecucion paralela: " + set_maximos_obtenidos.__str__())


if __name__ == '__main__':
    main()
