
#Los decoradores son una característica poderosa en Python que permiten modificar o extender el comportamiento de funciones o métodos de una manera sencilla y reutilizable. Los decoradores se utilizan comúnmente para agregar funcionalidades a funciones sin modificar su código interno. 




# Definir un decorador
def abrir_negocio(horario):
    def abrir():
        print("Comprobar que el horario sea 8AM")
        horario()
        print("Prepararse para abrir")
    return abrir


# Aplicar el decorador a una función
@abrir_negocio
def negocio():
    print("Negocio abierto!")

# Llamar a la función decorada
negocio()



#Decorador Property, el decorador property nos facilita la vida a la hora de manejar setter y getters. Con tan solo poner que un metodo es property ya nos da acceso a ese atributo privado, no vas a crear una funcion, si no una propiedad


class Persona:
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self. __apellido = apellido


    @property
    def nombre(self):               #Esto seria el getter
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre_nuevo):   #Setter es para actualizar, recordatorio
        self.__nombre = nombre_nuevo

    @nombre.deleter
    def nombre(self):
        self.__nombre                #Deletor elimina algo de memoria

    

persona = Persona("Facundo", "Alaniz")  #Aqui lo obtendriamos

persona.nombre = "Ernesto" #Aca podriamos actualizarlo si queremos

del persona.nombre #Si quitaramos el deleter, esto no funcionaria. Por eso siempre hay que agregarlo


n = persona.nombre

print(n)
    
#A simple viste se ven las ventajas de utilizar esta propiedad antes que usar el encapsulamiento que anteriormente vimos

    








