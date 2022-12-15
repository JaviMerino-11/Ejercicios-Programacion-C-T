# Escribe una clase para representar rectángulos, permitiendo almacenar el alto y el ancho, como atributos
# privados. Dota a la clase con métodos para devolver y cambiar los valores de la altura y anchura, así como para
# calcular el perímetro del mismo y también el área. Escribe un programa para ejemplificar su uso.

# Para ello, creo una clase que se instancie con dos atributos privados y protegidos -- alto y ancho.
# Creo un metodo para calcular el perimetro y otro para calcular el area.
# A partir del metodo magico __str__ -- devuelvo el valor del alto y del ancho
# Como los atributos estan protegidos, para cambiarlos debemos hacer uso del decorador de property y property setter


class Rectangulo:
    def __init__(self, alto: int, ancho: int):
        self.__alto = alto
        self.__ancho = ancho

    def __str__(self):
        return "Alto: %i\nAncho: %i" % (self.__alto, self.__ancho)

    def calcular_perimetro(self):
        perimetro = 2 * self.__alto + 2 * self.__ancho

        return perimetro

    def calcular_area(self):
        area = self.__ancho * self.__alto

        return area

    @property
    def altura(self):
        return self.__alto

    @altura.setter
    def altura(self, alto_nuevo: int):
        self.__alto = alto_nuevo

    @property
    def anchura(self):
        return self.__ancho

    @anchura.setter
    def anchura(self, ancho_nuevo: int):
        self.__ancho = ancho_nuevo


def main():
    alto = int(input("Introduzca el alto del rectangulo (valor entero): "))
    ancho = int(input("Introduzca el ancho del rectangulo (valor entero): "))

    rectangulo_1 = Rectangulo(alto=alto, ancho=ancho)

    perimetro_rectangulo_1 = rectangulo_1.calcular_perimetro()
    area_rectangulo_1 = rectangulo_1.calcular_area()

    print("Los datos del rectangulo son: \n" + rectangulo_1.__str__())

    print(
        "El perimetro del rectangulo es %f\nEl area del rectangulo es %f" % (perimetro_rectangulo_1, area_rectangulo_1))

    # Le cambio el valor de los atributos que habia usado para instanciar la clase, por otros nuevos diferentes.
    rectangulo_1.altura = 4
    rectangulo_1.anchura = 7

    print("Se han modificado la altura y la anchura a %i y %i" % (rectangulo_1.altura, rectangulo_1.anchura))


if __name__ == '__main__':
    main()
