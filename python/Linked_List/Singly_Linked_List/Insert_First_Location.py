class Node :
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(11)
head.next = Node(12)
head.next.next = Node(13)

def Insert_at_first(head, data) :
    new_head = Node(data) 
    new_head.next = head
    return new_head

def printList_By_recursion(head) :
    if head == None :
        print(None)
        return
    
    print(head.data, end="==>")
    printList_By_recursion(head.next)


head = Insert_at_first(head, 1)
printList_By_recursion(head)

head2 = None

head2 = Insert_at_first(head2, 101)
printList_By_recursion(head2)
