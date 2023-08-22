"""
Duck Typing en Python
El duck typing o tipado de pato es un concepto relacionado con la programación que aplica a ciertos lenguajes orientados a objetos, y que tiene origen en la siguiente frase:

If it walks like a duck and it quacks like a duck, then it must be a duck

Lo que se podría traducir al español como. Si camina como un pato y habla como un pato, entonces tiene que ser un pato.

¿Y qué relación tienen los patos con la programación? Pues bien, se trata de un símil en el que los patos son objetos y hablar/andar métodos. Es decir, que si un determinado objeto tiene los métodos que nos interesan, nos basta, siendo su tipo irrelevante.

"""

#El concepto de duck typing se fundamenta en el razonamiento inductivo, donde una serie de premisas apoyan la conclusión, pero no la garantizan. Si vemos a un animal que parece un pato, habla como tal y anda como tal, sería razonable pensar que se trata de un pato, pero sin un test de ADN nunca estaríamos al cien por cien seguros.

#Una vez entendido el origen del concepto, veamos lo que realmente significa esto en Python. En pocas palabras, a Python le dan igual los tipos de los objetos, lo único que le importan son los métodos.

#Definamos una clase Pato con un método hablar().

class Pato:
    def hablar(self):
        print("¡Cua!, Cua!")

p = Pato()
p.hablar()
# ¡Cua!, Cua!


#Hasta aquí nada nuevo, pero vamos a definir una función llama_hablar(), que llama al método hablar() del objeto que se le pase.


def llama_hablar(x):
    x.hablar()

#Como puedes observar, en Python no es necesario especificar los tipos, simplemente decimos que el parámetro de entrada tiene el nombre x, pero no especificamos su tipo.

#Cuando Python entra en la función y evalúa x.hablar(), le da igual el tipo al que pertenezca x siempre y cuando tenga el método hablar(). Esto es el duck typing en todo su esplendor.    

p = Pato()
llama_hablar(p)
# ¡Cua!, Cua!

class Perro:
    def hablar(self):
        print("¡Guau, Guau!")

class Gato:
    def hablar(self):
        print("¡Miau, Miau!")

class Vaca:
    def hablar(self):
        print("¡Muuu, Muuu!")


def llamar_perro(x):
    x.hablar()

perro = Perro()
gato = Gato()

llamar_perro(perro)

gato.hablar()


#Otra forma de verlo

lista = [Perro(), Gato(), Vaca()]
for animal in lista:
    animal.hablar()

# ¡Guau, Guau!
# ¡Miau, Miau!
# ¡Muuu, Muuu!