class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = False
        decreasing = False

        for index in range(1,len(nums)):
            if nums[index] > nums[index - 1]:
                increasing = True
            if nums[index] < nums[index - 1]:
                decreasing = True

        return not(increasing and decreasing) 