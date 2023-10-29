class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1 for val in nums]

        postfix = [1 for val in nums]

        for index in range(1,len(nums)):
            prefix[index] = prefix[index-1] * nums[index - 1]

        for index in reversed(range(len(nums)-1)):
            postfix[index] = postfix[index+1] * nums[index + 1]

        return [ prefix[index] * postfix[index] for index in range(len(nums))]