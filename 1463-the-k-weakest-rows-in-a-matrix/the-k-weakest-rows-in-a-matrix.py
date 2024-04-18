import queue

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        store = {}
        for row_index in range(len(mat)):
            count = 0
            for number in mat[row_index]:
                if number == 1:
                    count += 1
            
            if count not in store:
                store[count] = queue.Queue()
                store[count].put(row_index)
            else:
                store[count].put(row_index)

        ans = []
        keys = list(store.keys())
        keys.sort()
        for val in keys:
            if len(ans) == k:
                return ans
            while(store[val].qsize() > 0):
                ans.append(store[val].get())
                if len(ans) == k:
                    return ans
            

        return ans
