# Definición de la clase Persona
class Persona():
    def __init__(self, nombre, apellido):
        self.nombre = nombre  # Atributos públicos
        self.apellido = apellido  

    def hola(self): 
        print(f"Bienvenido {self.nombre}!")  


# Definición de la clase empleo que hereda de Persona
class empleo(Persona):
    def __init__(self, nombre, apellido, edad, profesion, añosexp):
        super().__init__(nombre, apellido)  # Llama al constructor de la clase padre (Persona)
        self.edad = edad 
        self.profesion = profesion  
        self.aniosexp = añosexp  #agregamos nuevos atributos


# Creación de una instancia de la clase empleo
persona1 = empleo("Ricardo", "Milos", "24", "Abogado", 2)

# Acceso a los atributos y métodos de la instancia persona1

print(persona1.nombre, persona1.apellido, persona1.edad, persona1.profesion, persona1.aniosexp)


persona1.hola() 
