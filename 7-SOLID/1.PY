
#SOLID es un acrónimo que representa cinco principios fundamentales de diseño en la programación orientada a objetos y la ingeniería de software. Estos principios buscan guiar la creación de software de alta calidad, mantenible y escalable. Fueron introducidos por Robert C. Martin y representan una guía para construir sistemas que sean fáciles de entender, extender y mantener.

"""

Principio de Responsabilidad Única (SRP - Single Responsibility Principle):
Este principio establece que una clase debe tener una única razón para cambiar, es decir, debe tener una única responsabilidad. Cada clase debe tener un solo propósito y no debe estar sobrecargada con múltiples funciones o responsabilidades.

Principio de Abierto/Cerrado (OCP - Open/Closed Principle):
Este principio establece que las entidades de software (clases, módulos, funciones, etc.) deben estar abiertas para la extensión pero cerradas para la modificación. En otras palabras, se debe poder agregar nuevas funcionalidades sin alterar el código existente.

Principio de Sustitución de Liskov (LSP - Liskov Substitution Principle):
Este principio establece que las instancias de una clase derivada deben poder ser sustituidas por instancias de la clase base sin afectar la integridad del programa. En resumen, las clases derivadas deben ser compatibles con las clases base y respetar su comportamiento.

Principio de Segregación de Interfaces (ISP - Interface Segregation Principle):
Este principio establece que ninguna clase debe ser forzada a implementar interfaces que no utiliza. En lugar de tener interfaces grandes y monolíticas, se deben crear interfaces más pequeñas y específicas para que las clases solo implementen lo que necesitan.

Principio de Inversión de Dependencia (DIP - Dependency Inversion Principle):
Este principio establece que los módulos de alto nivel no deben depender de módulos de bajo nivel, sino que ambos deben depender de abstracciones. Además, las abstracciones no deben depender de los detalles, sino que los detalles deben depender de las abstracciones. Esto promueve la creación de código flexible y reutilizable.


"""