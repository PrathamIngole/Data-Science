class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def printLL(head) :
    if head == None :
        print("list is empty : ") 
    
    temp = head 
    
    while temp != None :
        print(temp.data, end=" ==> ") 
        temp = temp.next
    print(None)

def insert_at_particular_position(head, data, pos) :
    # position is invalid then 
    if pos < 1 :
        print("invalid position")
        return head
    
    # position at the starting 
    if pos == 1 :
        node = Node(data) 
        node.next = head
        return node
    
    if head is None :
        print("pos out of range")
        return head
    
    temp = head
    cur = 1

    while cur < pos - 1 :
        if temp.next is None :
            print("position is out of range") 
            return head
        temp = temp.next
        cur += 1

    new_node = Node(data) 
    new_node.next = temp.next
    temp.next = new_node

    return head





head = Node(101)
head.next = Node(102)
head.next.next = Node(103)
head.next.next.next = Node(104)
head = insert_at_particular_position(head, 105, 5)

printLL(head)   