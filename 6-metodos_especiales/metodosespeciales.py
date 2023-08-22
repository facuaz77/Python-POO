#Así como el constructor, __init__, existen diversos métodos especiales que si están definidos en nuestra clase, Python los llamará por nosotros cuando se utilice una instancia en situaciones particulares.

"""
son métodos predefinidos en Python que tienen nombres que comienzan y terminan con dos guiones bajos (por ejemplo, __init__, __str__, __add__). Estos métodos especiales permiten definir el comportamiento de las clases en diferentes contextos, como la inicialización, la representación en cadena, la operación de suma y muchos otros aspectos.

Algunos de los métodos especiales más comunes y útiles incluyen:

__init__(self, ...): Este es el método de inicialización, también conocido como constructor. Se llama automáticamente cuando se crea una nueva instancia de la clase y se utiliza para configurar los atributos iniciales.

__str__(self): Define la representación en cadena de una instancia cuando se utiliza la función str(). Suele usarse para imprimir información legible para los humanos.

__repr__(self): Define una representación más formal y detallada de una instancia cuando se utiliza la función repr(). Debe ser una representación que permita recrear el objeto.

__len__(self): Define el comportamiento de la función len() cuando se aplica a una instancia de la clase. Suele utilizarse en objetos que son colecciones o contenedores.

__add__(self, other): Define el comportamiento de la operación de suma (+). Puede utilizarse para realizar operaciones personalizadas en objetos.

__eq__(self, other): Define el comportamiento de la comparación de igualdad (==). Permite personalizar cómo se comparan dos objetos.

__lt__(self, other): Define el comportamiento de la comparación de menor que (<). Permite personalizar cómo se comparan objetos para ordenarlos.

__getitem__(self, key): Define el comportamiento de la indexación (self[key]) en objetos que son iterables.

__setitem__(self, key, value): Define el comportamiento de la asignación (self[key] = value) en objetos que son mutables y admiten indexación.

__call__(self, ...): Permite que una instancia de la clase se comporte como una función, lo que significa que puede ser llamada como si fuera una función.

"""

from typing import Any


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Nombre de la persona: {self.nombre}"

    def __add__(self, other):
        suma_edades = self.edad + other.edad
        return Persona(self.edad + other.edad, suma_edades)
    
    def __eq__(self, other):
        return self.nombre == other.nombre
    
    def __lt__(self, other):
        return self.edad < other.edad
    
    def __ge__(self, other):
        return self.edad > other.edad
    
    

# Crear instancias de Persona
persona1 = Persona("Alice", 25)
persona2 = Persona("Bob", 30)

# Sobrecarga de operador de suma

suma = persona1 + persona2

#comprobar
comprobacion = persona1 == persona2

#menor que

x = persona1 < persona2

z = persona1 > persona2

print(suma.edad)
print(comprobacion)
print(x)
print(z)



    
