class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # #Appraoch1->Time limit Exceeded
        # result = [0 for val in range(len(nums))]

        # for index in range(len(nums)):
        #     curr = 1
        #     for val in range(len(nums)):
        #         if val == index:
        #             continue
        #         curr *= nums[val]

        #     result[index] = curr
            
        # return result

        #Approach2
        prefix = [1 for val in range(len(nums))]
        postfix = [1 for val in range(len(nums))]

        for index in range(len(nums)):
            if index == 0:
                continue
            prefix[index] = prefix[index - 1] * nums[index - 1]

        for index in reversed(range(len(nums))):
            if index == len(nums) - 1:
                continue
            postfix[index] = postfix[index + 1] * nums[index + 1]

        for val in range(len(postfix)):
            postfix[val] = postfix[val] * prefix[val]

        return postfix



