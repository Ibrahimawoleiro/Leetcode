import random
class RandomizedSet:

    def __init__(self):
        self.store = {}
        self.arr = []
    def insert(self, val: int) -> bool:
        if val not in self.store:
            self.arr.append(val)
            self.store[val] = len(self.arr) - 1
            return True
        else:
            return False
    def remove(self, val: int) -> bool:
        if val in self.store:
            index = self.store[val]
            if index !=  len(self.arr) - 1:
                last = self.arr.pop()
                self.arr[index] = last
                self.store[last] = index
            else:
                curr = self.arr.pop()
            
            del self.store[val]
            return True
        else:
            return False
    def getRandom(self) -> int:
        n = len(self.arr)
        r = random.randint(1, n)
        return self.arr[r - 1]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()