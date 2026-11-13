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

print(a)

