class Node :
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(11)
head.next = Node(12)
head.next.next = Node(13)

def insert_at_last(head, data) :

    if head == None :
        return Node(data)
    
    temp = head
    while temp.next != None :
        temp = temp.next

    temp.next = Node(data)
    return head

def printList_By_recursion(head) :
    if head == None :
        print(None)
        return
    
    print(head.data, end="==>")
    printList_By_recursion(head.next)


head = insert_at_last(head, 1)
printList_By_recursion(head)

head2 = None
printList_By_recursion(head2)

head2 = insert_at_last(head2, 101)
printList_By_recursion(head2)