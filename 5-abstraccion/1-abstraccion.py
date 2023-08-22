#La abstraccion es un concepto que se basa en que los desarrolladores debemos ocultar lo escencial de nuestro codigo y mostrar lo mas relevante y entendible para los usuarios, por ejemplo un celular tiene miles de funciones, esta programado para que el usuario con tan solo tocar una app esta se abra y sea utilizada, los widgets funcionan con tan solo activar nuestra ubicacion y ver el clima, la linterna funciona con tan solo presionar el icono,  etc
#"Lo escencial, es invisible a los ojos"
# Otra definicion: La abstracción permite manejar la complejidad al ocultar detalles internos y resaltar solo lo que es relevante para el usuario o el desarrollador. Se utiliza para crear modelos o representaciones de objetos o sistemas en niveles de detalle apropiados para una tarea específica.


class Auto:
    def __init__(self):
        self._estado = "Apagado"

    def encender(self):
        self._estado = "Encendido"
        print("Poniendo en marcha!")

    def conducir(self):
        if self._estado == "Apagado":
            self.encender()
            print("Preparando...")
        print("Conduciendo!")


auto = Auto()


      


