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

def delete_from_last(head) :
    if head == None :
        print("no element to delete from the list")
        return head
    
    if head.next == None :
        return None
    
    temp = head 
    while temp.next.next != None :
        temp = temp.next
        
    temp.next = None

    return head


head = Node(10)
head.next = Node(11)
head.next.next = Node(12)
head.next.next.next = Node(13)
head.next.next.next.next = Node(14)

printLL(head)

print("deleting element at first")
head = delete_from_last(head)
printLL(head)

print("deleting element at first")
head = delete_from_last(head)
printLL(head)

print("deleting element at first")
head = delete_from_last(head)
printLL(head)

print("deleting element at first")
head = delete_from_last(head)
printLL(head)

print("deleting element at first")
head = delete_from_last(head)
printLL(head)