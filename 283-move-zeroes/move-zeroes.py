class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i = j = 0

        while i < len(nums):

            while i < len(nums) and nums[i] == 0:

                i += 1

            if i == len(nums):
                break
            
            while j < i and nums[j] != 0:
                j += 1
            
            if nums[j] == 0:

                nums[i], nums[j] = nums[j] , nums[i]
            
            else:
                i += 1

