
class DynamicArray:

    def __init__(self):
        self.length = 0
        self.capacity = 1
        self.data = [None] * self.capacity

    def append(self, value):

        # Comprobamos si el array está lleno
        if self.length == self.capacity:
            self.resize()

        # Guardamos el elemento en la primera posición libre
        self.data[self.length] = value

        # Aumentamos el número de elementos
        self.length += 1

    def resize(self):

        # Duplicamos la capacidad
        new_capacity = self.capacity * 2

        # Creamos un nuevo array vacío
        new_data = [None] * new_capacity

        # Copiamos los elementos del array antiguo
        for i in range(self.length):
            new_data[i] = self.data[i]

        # Sustituimos el almacenamiento antiguo
        self.data = new_data

        # Actualizamos la capacidad
        self.capacity = new_capacity


# Prueba del programa
arr = DynamicArray()

for i in range(10):
    arr.append(i)

    print(
        f"Longitud: {arr.length}, "
        f"Capacidad: {arr.capacity}, "
        f"Datos: {arr.data}"
    )
