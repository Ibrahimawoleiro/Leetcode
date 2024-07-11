import heapq
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        store = {}
        rank = []
        for num in nums:
            if num in store:
                store[num] += 1
            else:
                store[num] = 1

        for key, val in store.items():
            heapq.heappush(rank, (-val, key))

        operations = 0
        while rank:
            curr = heapq.heappop(rank)
            freq = -curr[0]
            val = curr[1]
            if freq < 3 and freq < 2:
                return -1

            if freq % 3 == 0 and freq >= 3:
                freq -= 3
                if freq > 0:
                    heapq.heappush(rank, (-freq, val))
            elif freq >= 2:
                freq -= 2
                if freq > 0:
                    heapq.heappush(rank, (-freq, val))

            operations += 1

        return operations

            