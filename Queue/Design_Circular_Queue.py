class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [[0] for i in range(k)]
        self.head, self.tail = -1, -1
        self.k = k
        
    def isFull(self) -> bool:
        if ((self.tail + 1) % self.k) == self.head:
            return True
        return False

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.isEmpty():
            self.head = 0
            
        self.tail = (self.tail + 1) % self.k;
        self.queue[self.tail] = value;
        return True
    
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        if self.head == self.tail:
            self.head, self.tail = -1, -1
            return True
        
        self.head = (self.head + 1) % self.k;
        return True;
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        if self.head == -1:
            return True
        return False


# FIFO

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
