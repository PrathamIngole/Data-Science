class Node :
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        

class Stack : 
    def __init__(self):
        self.head = None 
        self.count = 0

    def push(self, data) :
        self.head = Node(data, self.head)
        self.count += 1
        return
    
    def pop(self) :
        if self.isempty() :
            return None
        val = self.head.data
        self.head = self.head.next
        self.count -= 1
        return val

    def peek(self) :
        if self.isempty() :
            return None
        return self.head.data
        
    def size(self) :
        return self.count

    def isempty(self) :
        return self.count == 0
    
    def display(self) :
        if self.isempty() :
            print("stack is empty")
            return
        temp = self.head
        while temp :
            print(temp.data) 
            temp = temp.next
        print()
        return
    
    def sortStack(self) :
        if not self.isempty() :
            temp = self.pop()
            self.sortStack()
            self.sortedInsertion(temp)
        return

    def sortedInsertion(self, data) :
        if self.isempty() or self.head.data <= data :
            self.push(data)
            return 
        temp = self.peek()
        self.pop()
        self.sortedInsertion(data)
        self.push(temp)
    
    def reverseStack(self) :
        if self.isempty() or self.head.next == None :
            return 
        curr = self.head
        prev = None 
        while curr :
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        self.head = prev
        return

    def bottomInsert(self, data) :
        if self.isempty() :
            self.push(data) 
            return
        if self.head.next == None :
            self.head.next = Node(data)
            self.count += 1
            return 
        temp = self.head 
        while temp.next :
            temp = temp.next
        temp.next = Node(data)
        self.count += 1


            

            
        

s = Stack()
s.display()
s.push(11)
s.push(802)
s.push(34)
s.push(69)
s.push(26)
s.push(3)
s.push(8)
print("size of stack : ",s.size())
print("peek : ",s.peek())
# print("is empty : ",s.isempty())
s.display()
print("poped : ",s.pop())
s.display()
print("peek : ",s.peek())
print("size of stack : ",s.size())
s.sortStack()
print("peek : ",s.peek())
s.display()
print("is empty : ",s.isempty())
s.reverseStack()
s.display()
s.bottomInsert(1000)
s.display()