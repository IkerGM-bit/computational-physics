class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None
        pass
    
a = Node(10)
b = Node(20)
c = Node(30)



a.next = b
b.next = c

current = a


# Completa el bucle:
while current != None:
    print(current.value)
    current = current.next
