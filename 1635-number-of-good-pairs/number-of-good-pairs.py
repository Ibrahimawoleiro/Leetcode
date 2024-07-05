class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        store = {}
        ans = 0
        for num in nums:
            if num in store:
                store[num] += 1

            else:
                store[num] = 1

        for val in store.values():
            if val >= 2:
                ans += (val * (val - 1)) / 2

        return int(ans)