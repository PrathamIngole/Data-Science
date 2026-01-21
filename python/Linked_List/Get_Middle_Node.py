class Node :
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)
head.next = Node(11)
head.next.next = Node(12)
head.next.next.next = Node(13)
head.next.next.next.next = Node(14)
head.next.next.next.next.next = Node(15)
head.next.next.next.next.next.next = Node(16)
head.next.next.next.next.next.next.next = Node(17)



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

def middleNode(head) : 

    n = countNode(head) 

    if n <= 2 :
        return f"no middle value available only {n} nodes are available"
    
    count = 1
    temp = head
    while count < n//2 :
        count += 1
        temp = temp.next
    
    return temp.data


printLL(head)
print("no. of nodes ",countNode(head))
print("middle : ",middleNode(head))