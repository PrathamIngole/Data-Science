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

def countNode(head) :

    if head == None :
        return 0
    
    count = 0
    temp = head

    while temp is not None :
        count += 1
        temp = temp.next

    return count


def delete_at_pos(head, pos) :
    if head == None :
        print("Linked List already Empty")
        return None
    
    if pos == 1 :
        head = head.next
        return head

    nodes_count = countNode(head)
    if pos > nodes_count :
        print("position out of range")
        return head
    
    count = 1 
    temp = head
    while count < pos - 1 :
        if temp.next.next == None :
            print("position out of bound")
            return head
        
        temp = temp.next
        count += 1

    temp.next = temp.next.next
    return head

head = Node(10)
head.next = Node(11)
head.next.next = Node(12)
head.next.next.next = Node(13)
head.next.next.next.next = Node(14)
printLL(head)

print("deleting element at 6th pos")
head = delete_at_pos(head, 6)
printLL(head)

print("deleting element at 3rd postion")
head = delete_at_pos(head, 3)
printLL(head)

print("deleting element at 1st")
head = delete_at_pos(head, 1)
printLL(head)

print("deleting element at 5th")
head = delete_at_pos(head, 5)
printLL(head)