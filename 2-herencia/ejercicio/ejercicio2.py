
class Animal:
    def comer(self):
        print("Comer")

class Mamifero(Animal):
    def amamantar(self):
        print("amamantar")


class Ave(Animal):
    def Volar(self):
        print('Volar')


class Murcielago(Mamifero,Ave):
    pass


m = Murcielago()

m.amamantar()
m.comer()
m.Volar()
    