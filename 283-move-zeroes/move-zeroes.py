class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        fast = 0
        slow = 0
        while(fast < len(nums)):
            if nums[fast] != 0:
                temp = nums[fast]
                nums[fast] = nums[slow]
                nums[slow] = temp
                slow+=1
            fast += 1
        