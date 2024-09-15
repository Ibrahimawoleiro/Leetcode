class Box:
    def __init__(self):
        self.arr = [None for _ in range(2)]

class Trie:
    def __init__(self):
        self.box = Box()

    def insert(self,val):
        curr = self.box
        #Loop through every bit of val
        #Add it to the trie
        for i in range(31, -1 , -1):
            if val & (1 << i):
                if curr.arr[1]:
                    curr = curr.arr[1]
                else:
                    new_box = Box()
                    curr.arr[1] = new_box
                    curr = new_box
            else:
                if curr.arr[0]:
                    curr = curr.arr[0]
                else:
                    new_box = Box()
                    curr.arr[0] = new_box
                    curr = new_box
    
    def get_max(self,val):
        result = 0
        curr = self.box
        for i in range(31, -1 , -1):
            if val & (1 << i):
                if curr.arr[0]:
                    result |= (1 << i)
                    curr = curr.arr[0]
                else:
                    curr = curr.arr[1]
            else:
                if curr.arr[1]:
                    result |= (1 << i)
                    curr = curr.arr[1]
                else:
                    curr = curr.arr[0]
        return result
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        for val in nums:
            trie.insert(val)
        ans = 0
        for val in nums:
            ans = max(ans, trie.get_max(val))
        return ans