class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for val in range(len(nums))]
        postfix = [1 for val in range(len(nums))]
        ans = [1 for val in range(len(nums))]
        for index in range(len(nums)):
            if index == 0:
                continue
            prefix[index] = prefix[index - 1] * nums[index - 1]

        for index in range(len(nums) - 1, -1, -1):
            if index == len(nums) - 1:
                continue
            postfix[index] = postfix[index + 1] * nums[index + 1]

        for index in range(len(nums)):
            ans[index] = postfix[index] * prefix[index]
        
        return ans
