#La programación es la actividad que se enfoca en organizar un conjunto de datos ordenados a seguir para ser ciertas cosas, esta definición puede utilizarse en muchos contextos. Pero en el área de informática la programación es fundamental para la relación entre ordenadores y los usuarios.

#En programación, se conocen como paradigmas de programación a los métodos usados para realizar determinadas tareas o proyectos. En otras palabras, son métodos de programación de software que sirven para resolver un problema de sistemas o para llegar a los resultados esperados.

#Un objeto es la instancia de una clase

#para definir una clase necesitamos utilizar la palabra reservada class
#Y es recomenado utilizar siempre Pascal Case, aunque utilizar camel y snake case son válidos también!


class Persona(): #Esto se almacena en la ram, podes comprobarlo almacenandolo en una variable y ejecutandolo
    nombre = "Facundo"
    apellido="Garcia"
    edad=25

#Podemos llamar a estos objetos de la siguiente manera
print(Persona.nombre)

#tambièn modificarlos

Persona.apellido="Alaniz"

print(Persona.apellido)


#Esto es una manera estatica de crear una clase, a medida que vayan identificando mas personas esta forma de realizarlo ya no sirve, es por eso que hay una manera de asignar muchas personas con una sola clase y es creando un metodo con sus respectivos atributos

class Personas:
    def __init__(self, Nombre, Apellido, Edad): #Se define el metodo con sus atributos
        self.Nombre = Nombre        #Se definen las propiedades (atributos es lo mismo)
        self.Apellido = Apellido    #Llamar self.apellido es lo mismo que llamar Persona.Apellido
        self.age = Edad           #También no necesariamente tiene que tener el mismo nombre pero por nomenclatura de Python es recomendable, al igual que las clases se definan en singular y no en Plural



persona1 = Personas("Fernando", "Alonso", "24") #De esta manera podes tener varias personas almacenadas con nuestra pequeña clase
persona2 = Personas("Robert", "Oppenheimer", 30)


print(persona1.Nombre)
print(persona2.Apellido)
print(persona2.age)







