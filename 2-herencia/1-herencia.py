#Pilar fundamental de la POO

#Permite crear clases que se reutilizan, extienden y modifican el comportamiento de otras clases



class Persona:
    def __init__(self, nombre, apellido, nacionalidad):
        self.n = nombre
        self.a=apellido            #Se crean los atributos
        self.na=nacionalidad

    def lugar(self):
        print("La aduana")


class registro(Persona): #Registro hereda todo lo que contenga la clase Persona
    pass 


persona1 = registro("Miguel", "Gonzales", "mexicano") #Se crea una instancia


persona1.lugar()
print("Nombre---Apellido---Nacionalidad")
print(persona1.n , persona1.a , persona1.na)