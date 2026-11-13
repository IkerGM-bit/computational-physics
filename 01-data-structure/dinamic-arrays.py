
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
        
    def get(self, index):
        if 0<= index < self.length:
            return self.data[index]            
        else:
            raise IndexError("Índice fuera de rango")
        
    def set(self, index, value):
        if index < 0 or index >= self.length:
            raise IndexError("Índice fuera de rango")
        else:
            self.data[index] = value
    
    def insert(self, index, value):

    # Comprobamos que el índice sea válido
        if index < 0 or index > self.length:
            raise IndexError("Índice fuera de rango")

    # Si no hay espacio, ampliamos la capacidad
        if self.length == self.capacity:
            self.resize()

    # Desplazamos los elementos hacia la derecha
        for i in range(self.length, index, -1):
            self.data[i] = self.data[i - 1]

    # Insertamos el nuevo valor
        self.data[index] = value

    # Aumentamos la longitud
        self.length += 1
    
    
    def remove(self, index):

    # Comprobamos que el índice sea válido
        if index < 0 or index >= self.length:
            raise IndexError("Índice fuera de rango")

    # Desplazamos los elementos hacia la izquierda
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]

    # Limpiamos la última posición ocupada
        self.data[self.length - 1] = None

    # Reducimos la longitud
        self.length -= 1


    
                
    
            
arr = DynamicArray()

for x in [10, 20, 30, 40]:
    arr.append(x)

arr.remove(1)

print(arr.data)
print(arr.length)
print(arr.capacity)