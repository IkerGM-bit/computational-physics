class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None
        pass


def append(self, value):

    new_node = Node(value)

    if self.head is None:
        self.head = new_node

    else:
        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    self.length += 1

lista = LinkedList()

lista.append(10)
lista.append(20)
lista.append(30)

current = lista.head

while current is not None:
    print(current.value)
    current = current.next