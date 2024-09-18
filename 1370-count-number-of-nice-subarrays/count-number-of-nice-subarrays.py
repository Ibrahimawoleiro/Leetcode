class Solution:
    def optimized(self,nums, goal):
        if goal == -1:
            return 0
        l = 0
        r = 0
        ans = 0
        total = 0
        while r < len(nums):
            total += nums[r]
            while total > goal:
                total -= nums[l]
                l += 1
            ans += r - l + 1
            r+=1
        return ans

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        arr = [1 if val % 2 == 1 else 0 for val in nums]
        x = self.optimized(arr, k)
        y = self.optimized(arr, k - 1)
        return x - y