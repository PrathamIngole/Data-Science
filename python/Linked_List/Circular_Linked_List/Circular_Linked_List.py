class Node :
    def __init__(self, data, next = None) :
        self.data = data
        self.next = next
    
class Cll :
    def __init__(self) :
        self.tail = None
        self.count = 0

    def size(self) :
        return self.count
    
    def isempty(self) :
        return self.count == 0
    
    def insert_at_begining(self, data) :
        if self.isempty() :
            self.tail = Node(data)
            self.tail.next = self.tail   
        else :   
            self.tail.next = Node(data, self.tail.next)
        self.count += 1

    def insert_at_end(self, data) :
        if self.isempty() :
            self.tail = Node(data)
            self.tail.next = self.tail
        else : 
            self.tail.next = Node(data, self.tail.next)
            self.tail = self.tail.next
        self.count += 1
        
    def insert_at_pos(self, data, pos) :
        if pos < 0 or pos > self.count :
            print("please insert at valid postion")
            return 
        
        if self.isempty() and pos == 0 :
            self.insert_at_begining(data)
        elif pos == self.count :
            self.insert_at_end(data)
        elif pos == 0 :
            self.insert_at_begining(data)
        else :
            p = 0 
            head = self.tail.next
            while p < pos - 1 :
                head = head.next
                p += 1
            head.next = Node(data, head.next)
            self.count += 1
    
    def delete_at_begining(self) :
        if self.isempty() :
            print("list is empty")
            return
        elif self.tail == self.tail.next :
            self.tail = None
        else :
            self.tail.next = self.tail.next.next
        self.count -= 1

    def delete_at_end(self) :
        if self.isempty() :
            print("list is empty")
            return
        elif self.tail == self.tail.next :
            self.tail = None
        else : 
            head = self.tail.next
            while head.next != self.tail :
                head = head.next
            head.next = head.next.next
            self.tail = head
        self.count -= 1

    def delete_at_pos(self, pos) :
        if pos < 0 or pos > self.count - 1 :
            print("enter valid position")
            return 
        if self.isempty() :
            print("list is already empty")
            return
        elif pos == 0 :
            self.delete_at_begining()
        elif pos == self.count - 1 :
            self.delete_at_end()
        else : 
            p = 0 
            head = self.tail.next
            while p < pos - 1 :
                head = head.next
                p += 1
            head.next = head.next.next
            self.count -= 1

    def delete_node(self, data) :
        if self.isempty() :
            print("list is already empty")
            return   
              
        if self.tail == self.tail.next :
            if self.tail.data == data :
                self.tail = None
                self.count -= 1
                return
            else :
                print("node not found")
                return
        
        if self.tail.next.data == data :
            self.delete_at_begining()
            return 
        
        head = self.tail.next 
        while head.next != self.tail :
            if head.next.data == data :
                head.next = head.next.next 
                self.count -= 1
                return
            head = head.next

        if self.tail.data == data :
            self.delete_at_end()
        else :
            print("node not found")          

    def display(self) :
        if self.isempty() :
            print("list is empty")
        else :
            head = self.tail.next 
            while head != self.tail :
                print(head.data,end = " --> ")  
                head = head.next 
            print(self.tail.data, " --> None")
    
    def search(self, data) :
        if self.isempty() :
            return False
        
        if self.tail.next.data == data :
            return True
        
        if self.tail.data == data :
            return True
        
        head = self.tail.next
        while head != self.tail :
            if head.data == data :
                return True
            head = head.next
        
        return False
        

            
    



cll = Cll()
cll.display()
print("inserting elements...")
cll.insert_at_begining(3)
# cll.insert_at_begining(23)
cll.insert_at_begining(34)
cll.insert_at_end(50)
cll.insert_at_end(5)
# cll.insert_at_begining(1)
cll.display()
cll.insert_at_pos(100, 0)
cll.display()
print("size of list : ", cll.size())
print("is list empty : ", cll.isempty())
print("deleting elements...")
cll.delete_at_begining()
cll.display()
# cll.delete_at_begining()
# cll.display()
# cll.delete_at_end()
# cll.display()
# cll.delete_at_end()
# cll.display()
# cll.delete_at_pos(2)
# cll.display()
# cll.delete_at_pos(0)
# cll.display()
cll.delete_node(24)
cll.display()
print("is element in the list : ", cll.search(55))
