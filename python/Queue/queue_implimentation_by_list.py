class Queue :
    def __init__(self) :
        self.queue = []
        self.count = 0 
    
    def Enqueue(self, data) :
        self.queue.append(data)
        self.count += 1

    def Dequeue(self) :
        if self.isempty() :
            print("queue is already empty")
            return 
        val = self.queue.pop(0)
        self.count -= 1
        return val

    def size(self) :
        return self.count
    
    def isempty(self) :
        return self.count == 0
    
    def peek(self) :
        if self.isempty() :
            return None
        return self.queue[-1]
    
    def display(self) :
        for i in self.queue :
            print(i, end="  ")
        print()

    def getFront(self) :
        if self.isempty() :
            return None
        return self.queue[0]

    def getRare(self) :
        if self.isempty() :
            return None
        return self.queue[-1]

    

q = Queue()
q.Enqueue(3)
q.Enqueue(4)
q.Enqueue(5)
q.Enqueue(7)
q.display()
q.Dequeue()
q.display()
