class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def printLL(head) :
    if head is None :
        print("list is empty: ") 
        return head
    temp = head 
    while temp != None :
        print(temp.data, end=" ==> ")
        temp = temp.next
    print(None)

def deleteElement(head, data) :
    if head is None :
        print("list is already empty")
        return head
    
    if head.data == data :
        head = head.next
        return head
    
    temp = head
    while temp.next != None :
        if temp.next.data == data :
            temp.next = temp.next.next
        temp = temp.next

    return head

head = Node(11)
head.next = Node(13)
head.next.next = Node(12)
head.next.next.next = Node(14)
head.next.next.next.next = Node(13)
head.next.next.next.next.next = Node(15)
printLL(head)

print("deleting an element at pos :")
head = deleteElement(head, 13)
printLL(head)