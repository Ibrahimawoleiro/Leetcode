class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #1
        x = (len(nums)* (len(nums) + 1) ) / 2
        y = sum(nums)
        return int(x - y)