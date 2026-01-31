class Stack :
    def __init__(self) :
        self.lst = []

    def push(self, ele) :
        self.lst.append(ele)

    def pop(self) :
        if len(self.lst) == 0:
            print("stack empty")
            return
        return self.lst.pop()
    
    def peek(self) :
        if self.isempty() :
            print("stack is empty")
            return
        
        print(self.lst[len(self.lst) - 1])
        return

    
    def display(self) :
        print("|             |")
        print("|             |")
        for i in range(-1, -(len(self.lst) +1), -1):
            print(f"|      {self.lst[i]}      |")
        print("|_____________|")

    def isempty(self) :
        return len(self.lst) == 0
    
    def size(self) :
        return len(self.lst)
    



s = Stack()
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print("peek funciton : ")
s.peek()
s.pop()
print("peek funciton : ")
s.peek()
s.display()
print("is empty : ", s.isempty())
print("size of stack : ", s.size())

        

