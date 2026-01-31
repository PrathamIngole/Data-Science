from collections import deque

class Queue :
    def __init__(self) :
        self.queue = deque()

    def size(self) :
        return len(self.queue)
    
    def isempty(self) :
        return len(self.queue) == 0
    
    def enqueue(self, data) :
        self.queue.append(data)

    def dequeue(self) :
        if self.isempty() :
            return None
        return self.queue.popleft()
    
    def display(self) :
        print(self.queue)

    
q = Queue()
print(q.size())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.display()
print(q.dequeue())
q.dequeue
q.dequeue()

q.display()

print(q.isempty())