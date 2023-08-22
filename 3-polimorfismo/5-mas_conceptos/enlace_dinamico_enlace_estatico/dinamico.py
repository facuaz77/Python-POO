"""

Enlace Dinámico:

En el enlace dinámico, la decisión sobre qué función o método se va a llamar se toma en tiempo de ejecución. Esto significa que la función o método que se ejecutará se determina durante la ejecución del programa, basándose en el tipo real del objeto que se está llamando.

En Python, debido a su tipado dinámico y polimorfismo, el enlace dinámico es la forma predeterminada de resolución de llamadas a métodos.

"""

class Vehiculo:
    def x(self):
        pass


class Auto(Vehiculo):
    def x(self):
        print("Es un Vehiculo")


class Moto(Vehiculo):
    def x(self):
        print("Es un Vehiculo!")

class Paraguas(Vehiculo):
    def x(self):
        print("No es un Vehiculo!")


a = Auto()
m = Moto()
p = Paraguas()

a.x()
m.x()
p.x()