import heapq
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        store_A = collections.Counter(nums)
        print(store_A)
        store_B = {}
        for key, value in store_A.items():
            if value not in store_B:
                store_B[value] = []
                heapq.heappush(store_B[value], -1 * key)
            else:
                heapq.heappush(store_B[value], -1 * key)
        ans = []
        keys = sorted(store_B.keys())
        for val in keys:
            while(len(store_B[val]) > 0):
                curr = heapq.heappop(store_B[val])
                [ans.append(-1 * curr) for val in range(val)]
        
        return ans