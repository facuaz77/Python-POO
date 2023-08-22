"""

La capacidad de tratar objetos de diferentes clases que están relacionados por una jerarquía de herencia como si fueran objetos de una misma clase base. Permite que las subclases hereden los atributos y métodos de la clase base y, por lo tanto, sean tratadas de manera uniforme a través de una interfaz común.

En resumen, el polimorfismo de método se centra en la implementación de métodos en diferentes clases con la misma firma (mover) pero diferentes comportamientos, mientras que el polimorfismo de herencia se centra en tratar objetos de diferentes clases como si fueran objetos de una misma clase base debido a su relación jerárquica. Ambos tipos de polimorfismo son fundamentales en la programación orientada a objetos y permiten escribir código más flexible y reutilizable.

"""

class Vehiculo:
    def mover(self):
        pass

class Auto(Vehiculo):
    def mover(self):
        return "El auto se está moviendo."

class Avion(Vehiculo):
    def mover(self):
        return "El avión está despegando."

# Función que utiliza el polimorfismo de herencia
def movimiento(v):
    print(v.mover())

auto = Auto()
avion = Avion()

movimiento(auto)  # Salida: El auto se está moviendo.
movimiento(avion) # Salida: El avión está despegando.
