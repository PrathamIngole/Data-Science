class Node :
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)
head.next = Node(11)
head.next.next = Node(12)
head.next.next.next = Node(13)

def printLL(head) :
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

printLL(head)
print(countNode(head))