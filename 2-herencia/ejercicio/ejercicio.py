#Error que experimente haciendo este ejercicio fue el de ponerle el mismo nombre a un atributo/metodo




class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def datos(self):
        print(f"{self.nombre} tiene {self.edad}")

    
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        super().datos()
        self.grado = grado

    def mostrar_grado(self):
        print(f"El estudiante esta en {self.grado}")

        

estudiante = Estudiante("Carlos", 15, "Tercer año")

estudiante.mostrar_grado()



    

