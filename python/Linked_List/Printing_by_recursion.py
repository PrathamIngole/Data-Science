# Creation of Linked List

class Node :
    def __init__(self, data):
        self.data = data
        self.next = None



head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

print("printing mannually")
print(head.data)
print(head.next.data)
print(head.next.next.data)


def printList_By_recursion(head) :
    if head == None :
        print(None)
        print(head)
        return 
    
    print(head.data, end="==>")
    printList_By_recursion(head.next)


print("\nprinting this mannually")
printList_By_recursion(head) 

print("for new data it would be like : ") 
head = None
head = Node(111) 
head.next = Node(222) 
head.next.next = Node(333)

printList_By_recursion(head)