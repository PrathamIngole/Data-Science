from collections import deque

class Stack :
    def __init__(self) :
        self.lst = deque()

    def push(self, ele) :
        self.lst.append(ele)

    def pop(self) :
        if len(self.lst) == 0:
            print("stack empty")
            return
        self.lst.pop()
    
    def display(self) :
        print("|             |")
        print("|             |")
        for i in range(-1, -(len(self.lst) + 1), -1) :
            print(f"|      {self.lst[i]}      |")
        print("|_____________|")

    def isempty(self) :
        return len(self.lst) == 0
    
    def peek(self) :
        print(self.lst[-1])
    
    def size(self) :
        return len(self.lst)
    
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.pop()
s.display()
print("is empty : ", s.isempty())
print("size of stack : ", s.size())
s.peek()