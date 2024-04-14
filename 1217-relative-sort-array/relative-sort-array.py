import queue
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        checker = set()
        for val in arr2:
            checker.add(val)
        q = []
        store = {}
        for val in arr1:
            if val not in checker:
                q.append(val)
                checker.add(val)
            if val not in store:
                store[val] = 1
            else:
                store[val] += 1
        
        ans = []
        for val in arr2:
            while(store[val] > 0):
                ans.append(val)
                store[val] -= 1
        q.sort()
        q.reverse()
        while(q):
            curr = q.pop()
            while(store[curr] > 0):
                ans.append(curr)
                store[curr] -= 1

        return ans

