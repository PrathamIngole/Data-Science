# Creation of Linked List
class Node :
    def __init__(self, data):
        self.data = data
        self.next = None

# defining print function for printing a linked list
def printlist(head) :
    temp = head
    if temp == None : 
        return "list is empty"
    while temp != None :
        print(temp.data, end=" ==> ")
        temp = temp.next 
    print(None)



head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

print("print using manuall way")

print(head.data)
print(head.next.data)
print(head.next.next.data)
print(head.next.next.next)

print("print using printlist function")

printlist(head) 