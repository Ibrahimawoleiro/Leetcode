class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = 0
        total = 0
        length = 0
        while r < len(nums):
            total += nums[r]
            while nums[r] * ((r - l) + 1) - total > k:
                print(l)
                total -= nums[l]
                l += 1
            length = max(length, (r - l)+ 1)
            r += 1
        return length