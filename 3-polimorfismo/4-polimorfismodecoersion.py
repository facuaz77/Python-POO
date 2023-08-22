#El polimorfismo de coerción ya viene implementado en python, ya que como mencionamos anteriormente es de tipado dinámico

n1 = 5
n2 = 17.5

sum = n1 + n2

print(sum) 

#Lo que sucede aqui es que el dato INT se convierte automaticamente en un Float y eso es una coerción automatica, la pregunta ahora es ¿Es la única tipo de coerción automatica que tiene Python? 
#No.

def coercion2(rango):
    for ran in rango:
        print(f"Recorriendo el dato: {ran}")


lista = [1,2,3,4,5,6,7,8,9]

lista2 = ["Robert", "Albert", "Isaac", "Jose", "Manuel"]

lista3 = "Facundo"

coercion2(lista3)

#En este ejemplo se ve otra vez Polimorfismo de coerción, todos comparten la misma función pero con diferentes tipos de datos

# Coerción en operaciones de comparación
valor_entero = 5
valor_flotante = 5.0

if valor_entero == valor_flotante:
    print("Los valores son iguales")

# Coerción en concatenación de cadenas
numero = 42
cadena = "El número es: " + str(numero)
print(cadena)