class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        prefix = [0 for num in range(len(nums))]

        postfix = [0 for num in range(len(nums))]

        total = 0

        for index in range(len(nums)):
            prefix[index] = total
            total += nums[index]

        total = 0

        for index in range(len(nums) - 1, -1, -1):
            postfix[index] = total
            total += nums[index]

        for index in range(len(nums)):
            if prefix[index] == postfix[index]:
                return index

        return -1
        