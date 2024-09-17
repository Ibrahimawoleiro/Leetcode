class Solution:
    def optimized(self, nums, k):
        l = 0
        r = 0
        ans = 0
        zero = 0
        while r < len(nums):
            if nums[r] == 0:
                zero += 1
            while zero > k:
                if nums[l] == 0:
                    zero -= 1
                l += 1
            ans  = max(ans, r - l + 1)
            r += 1
        return ans
    def longestOnes(self, nums: List[int], k: int) -> int:
        return self.optimized(nums, k)