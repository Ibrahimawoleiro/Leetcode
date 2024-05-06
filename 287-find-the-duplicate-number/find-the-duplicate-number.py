class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        for index in range(len(nums)):
            current_at_pos_val = nums[abs(nums[index])]
            if current_at_pos_val < 0:
                return abs(nums[index])
            else:
                nums[abs(nums[index])] *= -1

        return -1