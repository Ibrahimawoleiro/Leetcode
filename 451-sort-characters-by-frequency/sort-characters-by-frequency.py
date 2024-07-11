import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        store = {}
        rank = []
        for letter in s:
            if letter in store:
                store[letter] += 1
            else:
                store[letter] = 1
        
        for key, val in store.items():
            heapq.heappush(rank, (-val, key))
        
        ans = ''
        while rank:
            curr = heapq.heappop(rank)
            letter = curr[1]
            count = -curr[0]
            for i in range(count):
                ans += letter

        return ans