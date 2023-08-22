

class persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre     #Creamos las clases como lo hicimos anteriormente con sus respectivos atributos
        self.apellido=apellido
        self.edad=edad

    def bienvenida(self):
        print(f"Bienvenido {self.nombre}")



class profesion:
    def __init__(self, empleo, empresa, paga):
        self.empleo = empleo
        self.empresa = empresa
        self.paga = paga

    def empleo(self):
        print(f"Es {self.empleo} trabaja en la empresa {self.empresa} y recibe un salario de {self.paga}")
    
    def heredar(self):
        print(f"Suerte en tu nueva etapa trabajando en {self.empresa}")

    


class empleado(persona,profesion):
    def __init__(self , nombre, apellido, edad, empleo, empresa, paga ):
        persona.__init__(self,nombre,apellido,edad)
        profesion.__init__(self,empleo,empresa,paga)
        super().bienvenida() #Siempre que queramos llamar a un metodo de una clase padre es recomendable usar super()
        super().empleo() #Tambien podemos llamar a las clases hijas
    
    def saludos(self):
        print(f"{self.heredar()}") #Con el self hacemos referencia a esa misma clase y función


        



empleado1 = empleado("Facundo", "Alaniz", 20, "Programador", "PergaDevs", 100000)

empleado1.heredar()

print("------------------------------------------------------------------------------")

empleado2 = empleado("Robert", "Oppenheimer", 40, "Fisico", "Proyect los alámos", "10000USD" )

empleado2.heredar()

print("------------------------------------------------------------")

#Podemos verificar si es una subclase con la función issubclass

herencia = issubclass(persona, profesion) #Dara False porque no son subclases

#Con esta función podemos verificar si este objeto es una instacia de empleado
instancia = isinstance(empleado1, empleado) #Dara como resultado True


instacia2 = isinstance(empleado1,empleado) #True
#Ya que esta heredando de empleado 

print(herencia)
print("-------------------------")
print(instancia)
print("-------------------------")
print(instacia2)

        

