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
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        trie = Trie()
        ans = [-1 for _ in range(len(queries))]
        i = 0
        q = []
        for index in range(len(queries)):
            q.append([queries[index][0], queries[index][1], index])
        q.sort(key=lambda x: x[1])
        for query in q:
            value = query[0]
            upper_bound = query[1]
            index = query[2]
            while i < len(nums) and nums[i] <= upper_bound:
                trie.insert(nums[i])
                i += 1
            if i == 0:
                continue
            ans[index] = trie.get_max(value)
        return ans
            