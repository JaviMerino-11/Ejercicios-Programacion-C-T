# Escribe una clase Persona con atributos, edad, nombre y sexo, y dótala con métodos _str_, getters y setters para cada
# dato miembro. Crea también una clase Estudiante que herede de la clase Persona, con atributos grado que estudia y
# curso por el que va. Escribe los métodos correspondientes para acceder a dichos datos miembro. Sobreescribe el método
# __str__ apoyándote en el método de la superclase.

# Para ello, vamos a crear una clase que sera reconocida como clase PADRE (Persona), la cual mostrará los datos de
# instanciamiento usando el metodo magico __str__. Estos parametros se modificaran haciendo uso del decorador @property
# y @property.setter. Por otro lado, se va a crear una segunda clase (Estudiante) que heredará de la clase PADRE y
# dispondrá de los mismos parametros de instanciamiento que ella además de unos nuevos haciendo uso del metodo super.
# A la hora de mostrar los datos asociados al estudiante, se ha modificado el metodo __str__ del padre siempre que se
# llame a esta segunda clase y, además, se ha dejado comentado otra opción que se realizaria mediante la implementacion
# de dos metodos y ejecutandolos en el flujo principal.

class Persona:
    def __init__(self, edad: int, nombre: str, sexo: str):
        self.__edad = edad
        self.__nombre = nombre
        self.__sexo = sexo

    def __str__(self):
        return "Edad: %i\nNombre: %s\nSexo: %s" % (self.__edad, self.__nombre, self.__sexo)

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad_nueva: int):
        self.__edad = edad_nueva

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre_nuevo: str):
        self.__nombre = nombre_nuevo

    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, sexo_nuevo: str):
        self.__sexo = sexo_nuevo


class Estudiante(Persona):
    def __init__(self, grado_estudio: str, curso_actual: int, edad: int, nombre: str, sexo: str):
        super().__init__(edad, nombre, sexo)
        self.grado_estudio = grado_estudio
        self.curso_actual = curso_actual

    # def mostrar_datos_personales(self):
    #     print("Nombre: %s\nEdad: %i\nSexo: %s" % (self.nombre, self.edad, self.sexo))
    #
    # def mostrar_datos_academicos(self):
    #     print("Grado de estudio: %s\nCurso actual: %i" % (self.grado_estudio, self.curso_actual))

    def __str__(self):
        return "\nNombre: %s\nEdad: %i\nSexo: %s\nGrado de estudio: %s\nCurso actual: %i" % (
            self.nombre, self.edad, self.sexo, self.grado_estudio, self.curso_actual)


def main():
    nombre_persona_1 = input("Introduzca el nombre de persona deseado: ")
    edad_persona_1 = int(input("Introduzca la edad de la persona deseado: "))
    sexo_persona_1 = input("Introduzca el sexo de la persona deseado: ")

    persona_1 = Persona(edad=edad_persona_1, nombre=nombre_persona_1, sexo=sexo_persona_1)

    datos_persona_1 = persona_1.__str__()
    print("\nLos datos de la persona introducidos son:\n" + datos_persona_1)

    # Le cambio el valor de los atributos que habia usado para instanciar la clase, por otros nuevos diferentes.
    persona_1.edad = 24
    persona_1.nombre = "Antonia"
    persona_1.sexo = "Mujer"

    print("\nLos datos de la persona se han modificado a:\nEdad: %i\nNombre: %s\nSexo: %s" % (
        persona_1.edad, persona_1.nombre, persona_1.sexo))

    grado_estudio = input("Introduzca el grado que esté estudiando: ")
    curso_actual = int(input("Introduzca su curso academico actual: "))

    estudiante_1 = Estudiante(grado_estudio=grado_estudio, curso_actual=curso_actual, edad=edad_persona_1,
                              nombre=nombre_persona_1, sexo=sexo_persona_1)

    # estudiante_1.mostrar_datos_personales()
    # estudiante_1.mostrar_datos_academicos()

    print(estudiante_1.__str__())


if __name__ == '__main__':
    main()
