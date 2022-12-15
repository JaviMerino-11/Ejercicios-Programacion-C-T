# Escribe una clase para representar puntos en 2D (con datos miembro privados) que tenga un método que muestre las
# coordenadas, asigne valores a cada una de ellas y calcule la distancia entre dos puntos. Escribe un pequeño
# programa para ejemplificar su uso.

# Para ello, vamos a crear una clase con dos variables de instanciamiento protegidas y privadas para referenciar las
# coordenadas x e y. Definiremos 2 metodos para mostrar coordenadas y para calcular la distancia a otro par de puntos
# introducidos. El metodo para asignar cada una de ellas se hace con el metodo magico de instanciacion __init__

import numpy as np


class Puntos2D:
    def __init__(self, coord_x: int, coord_y: int):
        self.__coord_x = coord_x
        self.__coord_y = coord_y

    def mostrar_coordenadas(self):
        print("Las coordenadas introducidas son: (%i,%i)" % (self.__coord_x, self.__coord_y))

    def distancia_puntos(self, segundo_punto):
        distancia = np.sqrt(
            (self.__coord_x - segundo_punto.__coord_x) ** 2 + (self.__coord_y - segundo_punto.__coord_y) ** 2)
        return distancia


def main():
    coord_x_1 = int(input("PRIMER PUNTO: \nIntroduzca un numero entero para el valor de la coordenada x: "))
    coord_y_1 = int(input("PRIMER PUNTO: \nIntroduzca un numero entero para el valor de la coordenada y: "))

    coord_x_2 = int(input("SEGUNDO PUNTO: \nIntroduzca un numero entero para el valor de la coordenada x: "))
    coord_y_2 = int(input("SEGUNDO PUNTO: \nIntroduzca un numero entero para el valor de la coordenada y: "))

    primer_punto = Puntos2D(coord_x=coord_x_1, coord_y=coord_y_1)
    segundo_punto = Puntos2D(coord_x=coord_x_2, coord_y=coord_y_2)

    primer_punto.mostrar_coordenadas()
    segundo_punto.mostrar_coordenadas()

    distancia_puntos = primer_punto.distancia_puntos(segundo_punto=segundo_punto)

    print("La distancia entre (%i,%i) y (%i,%i) es %f" % (coord_x_1, coord_y_1, coord_x_2, coord_y_2, distancia_puntos))


if __name__ == '__main__':
    main()
