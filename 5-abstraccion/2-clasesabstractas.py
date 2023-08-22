"""
Propiedades de las clases abstractas
La primera propiedad de las clases abstractas es que no puede ser instanciadas. Simplemente proporciona una interfaz para las subclases derivadas y evitando así la duplicación de código.

Otra característica de estas clases es que no es necesario que tengan una implementación de todos los métodos necesarios. Pudiendo ser estos abstractos. Los métodos abstractos son aquellos que solamente tienen una declaración, pero no una implementación detallada de las funcionalidades.

Las clases derivadas de las clases abstractas debe implementar necesariamente todos los métodos abstractos para poder crear una clase que se ajuste a la interfaz definida. En el caso de que no se defina alguno de los métodos no se podrá crear la clase.

Resumiendo, las clases abstractas define una interfaz común para las subclases. Proporciona atributos y métodos comunes para todas las subclases evitando así la necesidad de duplicar código. Imponiendo además lo métodos que deber ser implementados para evitar inconsistencias entre las subclases.

Para poder crear clases abstractas en Python es necesario importar la clase ABC y el decorador abstractmethod del modulo abc (Abstract Base Classes). Un módulo que se encuentra en la librería estándar del lenguaje, por lo que no es necesario instalar. Así para definir una clase privada solamente se tiene que crear una clase heredada de ABC con un método abstracto.

"""

from abc import ABC, abstractclassmethod

class Animal(ABC):
    @abstractclassmethod
    def __init__(self, nombre,accion, especie):
        self._nombre = nombre
        self._accion= accion
        self._especie = especie

    @abstractclassmethod    
    def presentacion(self):
      pass

    
class Gato(Animal):
    def __init__(self, nombre, accion, especie):
       super().__init__(nombre, accion, especie)


    def presentacion(self):
        print(f"Hola soy un gatita! mi nombre es {self._nombre} y pertenezco a la especie de los {self._especie} y me gusta mucho {self._accion}")


class Perro(Animal):
    def __init__(self, nombre, accion, especie):

        super().__init__(nombre, accion, especie)

    def presentacion(self):
        print(f"Hola soy un perrito! me llamo {self._nombre} y pertenezco a los {self._especie}, lo que mas me gusta hacer es {self._accion} todo el dia!")



x = Gato("Mishina", "Dormir", "Felinos")
z = Perro("Bartolito", "Jugar", "Caninos")

x.presentacion()

z.presentacion()


#Como podemos ver las clases abstractas son muy limpias! es facil utilizar la plantilla para darle el uso que queramos.

#Esto es parecido a crear una clase y heredarla! pero usar clases abstractas da muchas ventajas, fomenta el polimorfismo, evita errores y es más seguro!

