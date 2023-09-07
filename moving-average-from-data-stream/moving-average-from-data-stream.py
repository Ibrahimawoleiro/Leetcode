class MovingAverage:

    def __init__(self, size: int):
        self.count = 0
        self.queue = deque()
        self.size = size

    def next(self, val: int) -> float:
        self.count+=1
        total = 0.0
        if(len(self.queue) < self.size - 1):
            self.queue.append(val)
            for number in self.queue:
                total+=number
            total/=self.count
            return total
        else:
            if(len(self.queue) == self.size):
                self.queue.popleft()
            self.queue.append(val)
            for number in self.queue:
                total+=number
            total/=self.size
            return total
        
                
                


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)