class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):

        # Creamos el nuevo nodo
        new_node = Node(value)

        # Caso 1: la lista está vacía
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        # Caso 2: ya existen nodos
        else:
            self.tail.next = new_node
            self.tail = new_node

        # Aumentamos la longitud
        self.length += 1


# Probamos nuestra lista
lista = LinkedList()

lista.append(10)
lista.append(20)
lista.append(30)

current = lista.head

while current is not None:
    print(current.value)
    current = current.next
