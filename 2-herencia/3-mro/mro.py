#El MRO Method Resolution Order es el proceso por el cual Python busca metodos y atributos en las clases, un aspecto crucial de la herencia!

#La MRO se calcula siguiendo el algoritmo C3, que prioriza el orden de herencia de izquierda a derecha. En nuestro ejemplo, la jerarquía es D -> C -> B -> A.


class A():
    def saludo(self):
        print("Hola desde A")


class B:
    def saludo(self):
        print("Hola desde B")

class C():
    def saludo(self):
        print("Hola desde C")

class D(C,B):
    def saludo(self):
        print("Hola desde D")
    


