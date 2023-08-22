#Este tipo de polimorfismo ocurre cuando diferentes clases tienen métodos con el mismo nombre pero diferentes parámetros o tipos de retorno. Python no admite la sobrecarga de métodos directamente, pero puedes simularla utilizando argumentos opcionales o *args y **kwargs. Este metodo de sobrecarga lo podemos ver en otros lenguajes como por ej: Java

class Calculadora:
    def suma(self, a, b, ):
        return a + b

    def suma(self, a, b, c):
        return a + b + c

calc = Calculadora()
print(calc.suma(2, 3))         # Esto generará un error, ya que solo se definió suma(a, b, c)
print(calc.suma(2, 3, 4))      # Salida: 9


#Para que funcione tendria que ser asi 
"""

class Calculadora:
    def suma(self, a, b, *args, **kwargs):
        if len(args) == 1:
            return a + b + args[0]
        else:
            return a + b

            



*args: Es una sintaxis especial que se utiliza en la definición de una función o método para capturar un número variable de argumentos posicionales en forma de una tupla. El nombre args es una convención, pero podrías usar cualquier otro nombre en su lugar. Los argumentos pasados después de los argumentos normales se empaquetan automáticamente en una tupla args.

**kwargs: Similar a *args, pero se utiliza para capturar un número variable de argumentos de palabra clave (argumentos nombrados) en forma de un diccionario. El nombre kwargs es una convención, pero al igual que con *args, podrías utilizar cualquier otro nombre.



            

"""
