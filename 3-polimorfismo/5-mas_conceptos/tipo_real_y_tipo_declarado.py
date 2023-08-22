"""
Tipo Real (Runtime Type): El tipo real se refiere al tipo actual del objeto en tiempo de ejecución, es decir, qué tipo de objeto es en ese momento en el flujo de ejecución del programa. Es importante tener en cuenta que en lenguajes de tipado dinámico como Python, el tipo real de un objeto puede cambiar durante la ejecución.

Tipo Declarado (Declared Type): El tipo declarado se refiere al tipo que se especifica en la declaración o anotación del objeto o variable. En algunos lenguajes de programación estáticos, como Java o C++, se espera que declares el tipo de un objeto o variable en tiempo de compilación, y este tipo declarado es utilizado para determinar la resolución de llamadas a métodos.

En Python, debido a su tipado dinámico y enlace dinámico predeterminado, no te preocupas mucho por el tipo declarado. Sin embargo, puedes usar anotaciones de tipo para indicar el tipo esperado de una variable o argumento, lo que puede ser útil para mejorar la legibilidad y el mantenimiento del código. Estas anotaciones son consideradas sugerencias y no afectan la resolución de llamadas a métodos.



"""
#Ejemplo de anotación de tipo en Python:

def suma(a: int, b: int) -> int:
    return a + b





