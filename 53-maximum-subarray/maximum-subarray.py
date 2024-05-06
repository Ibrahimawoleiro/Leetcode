class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_total = nums[0]
        current = nums[0]
        for index in range(len(nums)):
            if index == 0:
                continue
            if nums[index] + current > nums[index]:
                current += nums[index]
                if current > max_total:
                    max_total = current
            else:
                current = nums[index]
                if current > max_total:
                    max_total = current
        return max_total
                