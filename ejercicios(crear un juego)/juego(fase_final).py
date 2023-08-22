class Personaje:
    def __init__(self, nombre, poder, velocidad, daño):
        self.nombre = nombre
        self.poder = poder
        self.velocidad = velocidad
        self.daño = daño

    @classmethod
    def crear_personaje(cls):
        nombre = input("Ingrese el nombre del personaje: ")
        poder = int(input("Ingrese la fuerza del personaje: "))
        velocidad = int(input("Ingrese su velocidad: "))
        daño = int(input("Ingrese el daño de su personaje: "))
        return cls(nombre, poder, velocidad, daño)
    

    def pelea(self, other):
        if self.poder + self.velocidad + self.daño > other.poder + other.velocidad + other.daño:
            print(f"El poder de {self.nombre} es de {self.poder}, su velocidad es de {self.velocidad} y tiene un daño de {self.daño}!")
            print(f"{self.nombre} es el ganador!")
        else:
            print(f"El poder de {other.nombre} es de {other.poder}, su velocidad es de {other.velocidad} y tiene un daño de {other.daño}!")
            print(f"{other.nombre} es el ganador!")

def mostrar_personajes(personajes):
    print("Tus personajes:")
    for i, personaje in enumerate(personajes, start=1):
        print(f"{i}. Nombre: {personaje.nombre}, Poder: {personaje.poder}, Velocidad: {personaje.velocidad}, Daño: {personaje.daño}")

def menu():
    print("-----Escoja una opción-----")
    print("1. Crear personaje")
    print("2. Ver tus personajes")
    print("3. Combate!")
    print("4. Salir del programa")
    return int(input("Ingrese el número de la opción: "))

personajes = []

while True:
    try:
        opcion = menu()
        if opcion == 1 and len(personajes) < 10:
            nuevoPersonaje = Personaje.crear_personaje()
            personajes.append(nuevoPersonaje)
            print("Personaje creado exitosamente!")
        elif opcion == 2:
            mostrar_personajes(personajes)
            if len(personajes) == 0:
                print("Aun no hay personajes creados!")
        elif opcion == 3:
            mostrar_personajes(personajes)
            if len(personajes) < 2:
                print("Necesitas al menos dos personajes para combatir")
            else:
                num1 = int(input("Seleccione el número del primer personaje: ")) - 1
                num2 = int(input("Seleccione el número del segundo personaje: ")) - 1
                if num1 < 0 or num2 < 0 or num1 >= len(personajes) or num2 >= len(personajes) or num1 == num2:
                    print("Selección inválida")
                else:
                    personaje1 = personajes[num1]
                    personaje2 = personajes[num2]
                    personaje1.pelea(personaje2)
        elif opcion == 4:
            print("¡Hasta luego!")
            break
        else:
            print('Opción inválida')

    except:
        print("Ha ocurrido un error... tal vez estás ingresando una letra!")
