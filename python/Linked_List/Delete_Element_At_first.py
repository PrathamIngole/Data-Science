class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def printLL(head) :
    if head == None :
        print("list is empty") 
        return
    
    temp = head 
    
    while temp != None :
        print(temp.data, end=" ==> ") 
        temp = temp.next
    print(None)

def delete_from_start(head) :
    if head == None :
        print("no element to delete from the list")
        return head
    head = head.next
    return head


head = Node(10)
head.next = Node(11)
head.next.next = Node(12)
head.next.next.next = Node(13)
head.next.next.next.next = Node(14)

printLL(head)

print("deleting element at first")
head = delete_from_start(head)
printLL(head)

print("deleting element at first")
head = delete_from_start(head)
printLL(head)

print("deleting element at first")
head = delete_from_start(head)
printLL(head)

print("deleting element at first")
head = delete_from_start(head)
printLL(head)

print("deleting element at first")
head = delete_from_start(head)
printLL(head)
