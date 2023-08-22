
class Estudiante():
    def __init__(self, nombre, edad, grado):
        self.n = nombre
        self.e = edad
        self.g = grado



nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))  
grado = str (input ("Ingrese el grado de estudio actual: "))


alumno = Estudiante(nombre, edad, grado)

print(f"El alumno {alumno.n} de {alumno.g} tiene una edad de {alumno.e} años.")


if alumno.e > 15:
    print('Secundario superior')
else:
    if 12 <= alumno.e <= 14:
        print("Secundaria básica")
    else:
        print("Primaria o inferior, no deberias estar en secundaria! (A no ser que seas un genio)")

    
    