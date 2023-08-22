#Un metodo es una funcion, una accion que contemplara al atributo establecido en una clase


class Gato:
    def __init__(self, nombre, accion):
        self.nombre = nombre  #atributo
        self.accion = accion

    
    def acciones(self):               #Sus metodos, recordar hacer siempre el self para hacer referencia al objeto
        print(f"{self.nombre} {self.accion}")

    def presentacion(self):
        print(f"Hola soy un gato y me llamo {self.nombre}")
        



gato1 = Gato("Pepito", "Duerme")

gato1.acciones()