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
                print(total, l)
                total -= nums[l]
                l += 1
            ans += r - l + 1
            r+=1
        return ans

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        x = self.optimized(nums, goal)
        y = self.optimized(nums,  goal - 1)
        ans = x - y
        return ans