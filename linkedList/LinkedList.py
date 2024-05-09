class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d

def display(head):
    current = head
    while (current != None):
        print(current.data)
        current = current.next

display(a)

