#El polimorfismo permite que diferentes clases sean tratados de manera uniforme a través de una interfaz común, es decir que si tenemos una clase Perro con un metodo de sonido que este sea ladrar y otra clase gato con el mismo metodo (sonido) pero que este imprima maullar, el polimorfismo permitira que cuando ejecutemos la clase perro este muestre en pantalla que esta ladrando. Gracias al Polimorfismo nuestro codigo se hace mas flexible y reutilizable

class Animal:
    def sonido(self):
        pass

class Perro(Animal):
    def sonido(self):
        return "Woof!"

class Gato(Animal):
    def sonido(self):
        return "Meow!"

def sonido_animal(animal):
    print(animal.sonido())

perro = Perro()
gato = Gato()

sonido_animal(perro)  # Salida: Woof!
sonido_animal(gato)   # Salida: Meow!

#También se puede realizar de esta manera

#print(perro.sonido())
#print(gato.sonido())


#Quitando la clase Animal este codigo funcionaria igual, ya que python a diferencia de otros lenguajes es de tipado dinamico por lo que si el codigo seria de esta manera




class Perro():
    def sonido(self):
        return "Woof!"

class Gato():
    def sonido(self):
        return "Meow!"

        
perro = Perro()
gato = Gato()


print(perro.sonido())
print(gato.sonido())


#Funciona de igual manera y con menos lineas de codigo!



