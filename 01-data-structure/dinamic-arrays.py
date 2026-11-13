
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
            
            
        
        
        


arr = DynamicArray()

arr.append(10)
arr.append(20)
arr.append(30)

arr.set(1, 50)

print(arr.data)
exit()