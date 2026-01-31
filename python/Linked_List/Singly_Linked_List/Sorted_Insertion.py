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


def SortedInsertion(head, data) :
    if head is None :
        node = Node(data)
        return node
    
    new_node = Node(data) 
    temp = head 
    if temp.data > data :
        new_node.next = temp
        return new_node
    
    prev_temp = temp
    while temp.data <= data :
        if temp.next == None :
            temp.next = new_node
            return head
        prev_temp = temp
        temp = temp.next



    new_node.next = temp
    prev_temp.next = new_node

    return head

def SortedInsertionDesc(head, data) :
    if head is None :
        node = Node(data)
        return node
    
    new_node = Node(data) 
    temp = head 
    if temp.data < data :
        new_node.next = temp
        return new_node
    
    prev_temp = temp
    while temp.data >= data :
        if temp.next == None :
            temp.next = new_node
            return head
        prev_temp = temp
        temp = temp.next



    new_node.next = temp
    prev_temp.next = new_node

    return head

print("ascending order : ")
head = None
head = SortedInsertion(head, 100)
head = SortedInsertion(head, 110)
head = SortedInsertion(head, 120)
head = SortedInsertion(head, 130)
head = SortedInsertion(head, 140)
head = SortedInsertion(head, 150)
printLL(head)   
head = SortedInsertionDesc(head, 115)
printLL(head)   

print("descending order : ")
head = None
head = SortedInsertionDesc(head, 100)
head = SortedInsertionDesc(head, 110)
head = SortedInsertionDesc(head, 120)
head = SortedInsertionDesc(head, 130)
head = SortedInsertionDesc(head, 140)
head = SortedInsertionDesc(head, 150)
printLL(head)   
head = SortedInsertionDesc(head, 115)
printLL(head)   