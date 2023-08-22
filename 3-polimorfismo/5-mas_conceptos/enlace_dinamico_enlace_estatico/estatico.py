
"""

Enlace Estático:

En python no es posible este tipo de enlace pero es importante saberlo! este tipo de enlace se puede ver en C, Java, todo tipo de lenguaje que tenga tipado estatico

En el enlace estático, la decisión sobre qué función o método se va a llamar se toma en tiempo de compilación, en función del tipo declarado del objeto o variable. En Python, este enlace estático se puede simular utilizando tipos anotados o chequeo de tipos estáticos con herramientas externas.



"""

from typing import Type #se importa la libreria

class Animal:
    def sonido(self):
        pass

class Perro(Animal):
    def sonido(self):
        return "¡Woof!"

class Gato(Animal):
    def sonido(self):
        return "¡Meow!"

def hacer_sonar(animal: Type[Animal]): #Se simula
    print(animal.sonido())

perro = Perro()
gato = Gato()

hacer_sonar(perro)  # Salida: ¡Woof!
hacer_sonar(gato)   # Salida: ¡Meow!
