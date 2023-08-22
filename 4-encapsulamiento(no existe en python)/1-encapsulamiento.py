"""
En la Programación orientada a objetos, la encapsulación se refiere a la agrupación de datos con los métodos que operan en esos datos, o la restricción del acceso directo a algunos de los componentes de un objeto

Aunque Python no tiene las mismas palabras clave para definir el nivel de acceso, utiliza la convención de nombres con un guión bajo (por ejemplo, _variable) para indicar que un miembro debería tratarse como privado. Sin embargo, en Python, no hay restricciones reales en el acceso a los miembros, ya que la filosofía principal es "somos todos adultos aquí".

"""

#Ejemplo


class Persona:
    def __init__(self, nombre):
        self._nombre = nombre    #un solo _ significa clase privada, es posible acceder con un getter


    def get_nombre(self):
        return self._nombre
    

persona = Persona("Juan")

print(persona.get_nombre())# Un getter es un método que se utiliza para obtener el valor de un atributo privado de una clase. Proporciona acceso de solo lectura a ese atributo.



class Persona2:
    def __init__(self, nombre):
        self.__nombre = nombre #Dos guiones bajos __ significa que es una clase "ultra privada" por asi decirlo de alguna manera y es posible acceder con un setter

#Setter: Un setter es un método que se utiliza para asignar un valor a un atributo privado de una clase. Proporciona acceso de escritura a ese atributo.

    def setter_nombre(self, nuevo):
        self.__nombre = nuevo

    def get_nombre(self):
        return self.__nombre


# Usar el setter para cambiar el nombre
persona2 = Persona2("Jose")
persona2.setter_nombre("Antonio")  # Utilizamos el setter para cambiar el nombre
print(persona2.get_nombre())

#De esta manera podriamos modificar con un setter el atributo ultra privado



    


