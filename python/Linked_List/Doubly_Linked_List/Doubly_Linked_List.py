# defining node class
class Node :

    #defining node class constructor : 
    def __init__(self, data, next = None, prev = None) :
        self.data = data
        self.next = next
        self.prev = prev

# defining doubly Linked list class
class DoublyLinkedList :

    # defining the countructor to store head :
    def __init__ (self) :
        self.head = None
        self.tail = None
        self.count = 0 

    # defing the dender function __str__ :
    def __str__(self) :
        if self.head == None :
            return "list is empty" 
        
        out = ''
        temp = self.head
        while temp :
            out += f"{temp.data} <=> "
            temp = temp.next
        return out + "None"
    
    # number of nodes present method :
    def size(self) :
        print("list size is : ",self.count)
        return 
    
    # check if list is empty or not :
    def isEmpty(self) :
        print("is list empty : ",self.count == 0)
        return
    
    # display doubly linked list : 
    def display(self) :
        if self.head is None :
            print("List is Empty")
            return 
        
        temp = self.head
        print("list is : ")
        while temp :
            print(temp.data, end=" <=> ")
            temp = temp.next
        print(None)
        return 
    
    # display list recursively : 
    @staticmethod
    def displayRecursive(temp) :
        if temp == None :
            print(None)
            return 
        
        print(temp.data, end=" <=> ")
        return DoublyLinkedList.displayRecursive(temp.next)

    # creating Insert_at_Begining
    def Insert_at_Begining(self, data) :
        
        new_node = Node(data)
        self.count += 1

        if self.head is None :
            self.head = new_node
            self.tail = new_node
            return 
        
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        return 
        
    # creating Insert_at_End
    def Insert_at_End(self, data) :
        new_node = Node(data)
        self.count += 1
        if self.head == None :
            self.head = new_node
            self.tail = new_node
            return 
        
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node 
        return 
    
    # Insert at given location : 
    def Insert_at_Position(self, data, pos) :
        new_node = Node(data) 

        if pos > self.count +1 :
            print("Invalid Position\n")
            return 
        
        if pos == 1 :
            self.Insert_at_Begining(data)
            return 
        
        if pos == self.count + 1 :
            self.Insert_at_End(data)
            return
        
        temp = self.head
        curr = 1 
        while curr < pos :
            temp = temp.next
            curr += 1
        temp.prev.next = new_node
        new_node.prev = temp.prev
        new_node.next = temp
        temp.prev = new_node

        self.count += 1
        return 
    
    # delete at first :
    def Delete_at_Begining(self) :
        if self.head == None :
            print("\nlist empty delete not possible")
            return 
        
        self.head = self.head.next
        self.prev  = None
        self.count -= 1
        return  
    
    # delete from last :
    def Delete_at_Last(self) :
        if self.head == None :
            print("list already empty")
            return 

        if self.head.next == None :
            self.head = None
            self.tail = None
            self.count = 0
            return 

        self.tail = self.tail.prev
        self.tail.next = None
        self.count -= 1
        return 
    
    # delete form specific postion :
    def Delete_at_pos(self, pos) :
        if self.head == None :
            print("\n already empty")
            return 
        
        if pos < 1 or pos > self.count :
            print("position out of bound")
            return 
        
        if pos == 1 :
            self.Delete_at_Begining()
            return 
        
        if pos == self.count :
            self.Delete_at_Last()
            return 
        
        curr = 1
        temp = self.head
        while curr < pos :
            temp = temp.next
            curr += 1
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        self.count -= 1

        return 
    
    # delete a node :
    def Delete_Node(self, data) :
        if self.head is None :
            print("No element present")
            return 
        
        if self.head.data == data :
            self.Delete_at_Begining()
            return 
        
        if self.tail.data == data :
            self.Delete_at_Last() 
            return 
                
        if self.head == self.tail :
            if self.head.data == self.tail.data and self.tail.data == data :
                self.head = None
                self.tail = None
                self.count -= 1
                return
            else :
                print("element not exist")
                return 
        
        temp = self.head 
        last = None
        while temp :
            if temp.data == data :
                temp = temp.next
                temp.prev = last
                last.next = temp
                self.count -= 1
                return 
            last = temp
            temp = temp.next
        if temp == None :
            print("element not found")
            return 
    
    # copy list :
    def copyList(self) :
        if self.head is None :
            return None
        newList = DoublyLinkedList()

        if self.count == 1:
            newList.Insert_at_End(self.head.data)
            return newList
        
        temp = self.head
        while temp :
            newList.Insert_at_End(temp.data)
            temp = temp.next
        return newList

    # search element in Doubly linked list :
    def search(self, data) :
        if self.head == None :
            print("Element not present & list is empty")
            return
        
        if self.head.data == data :
            print("element found at positoin : ", 1)
            return
        
        if self.tail.data == data :
            print("element found at positoin : ", self.count)
            return

        temp = self.head
        pos = 1
        while temp :
            if temp.data == data :
                print("element found at positoin : ", pos)
                return
            temp = temp.next
            pos += 1

        print("Element not present")
        return 
            
    # search element using recursion :
    def searchRecusive(self, head, data, pos = 1) :
        if head == None :
            print("Element not found")
            return 
        if head.data == data :
            print("element found at positoin : ", pos)
            return 
        self.searchRecusive(head.next, data, pos+1)

    # reverse a doubly link list :
    def reverseList(self) :
        if self.head == None :
            print("list is empty")
            return 
        if self.head == self.tail :
            return 
        
        start = 1
        end = self.count

        startNode = self.head
        endNode = self.tail

        while start <= end :
            startNode.data, endNode.data = endNode.data, startNode.data
            startNode = startNode.next
            endNode = endNode.prev
            start += 1
            end -= 1
        
        return

            

if __name__ == "__main__" :
    dll = DoublyLinkedList()
    # dll.size()
    # dll.isEmpty()
    # dll.display()
    # print()
    dll.Insert_at_Begining(30)
    dll.Insert_at_Begining(20)
    dll.Insert_at_Begining(10)
    dll.Insert_at_End(40)
    dll.Insert_at_End(50)
    dll.Insert_at_End(60)
    dll.display()
    # dll.size()
    # dll.isEmpty()
    # print("\nrecursive display list is : ")
    # dll.displayRecursive(dll.head)
    # print("\nusing __str__ dender function : printing list")
    # print(dll)
    # dll.size()
    # print("\ninserting at specific location :")
    # # dll.Insert_at_Position(65, 3)
    # dll.size()
    # dll.Delete_at_Begining()
    # dll.size()
    # dll.Delete_at_Begining()
    # dll.size()
    # dll.Delete_at_Begining()
    # dll.size()
    # dll.Delete_at_Begining()
    # dll.size()
    # dll.Delete_at_Begining()
    # dll.size()
    # dll.Delete_at_Begining()
    # dll.size()
    # dll.Delete_at_Begining()
    # dll.size()
    # dll.Delete_at_Begining()
    # dll.size()
    # dll.display()
    # dll.Delete_at_Last()
    # dll.display()
    # dll.Delete_at_Last()
    # dll.display()
    # dll.Delete_at_pos(3)
    # dll.display()
    # dll.Delete_at_pos(1)
    # dll.display()
    # dll.Delete_at_pos(4)
    # dll.display()
    # dll.Delete_at_pos(2)
    # dll.display()
    # dll.Delete_at_pos(7)
    # dll.Delete_Node(70)
    # dll.display()
    # dll_2 = dll.copyList()
    # print("\noriginal : ")
    # dll.Delete_at_Begining()
    # dll.display()

    # print("\ncopied list : ")
    # dll_2.display()

    # dll.search(10)
    # dll.searchRecusive(dll.head, 70)
    print("\nreversing list")
    dll.reverseList()
    dll.display()