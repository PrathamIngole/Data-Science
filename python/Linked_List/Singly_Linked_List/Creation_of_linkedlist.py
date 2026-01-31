# Creation of Linked List

class Node :
    def __init__(self, data):
        self.data = data
        self.next = None



head = Node(10)
head.next = Node(20)
head.next.next = Node(30)


print(head.data)
print(head.next.data)
print(head.next.next.data)
print(head.next.next.next)