class Solution:
    def rob(self, nums: List[int]) -> int:
        # #Approach 1
        # if len(nums) == 1:
        #     return nums[0]
        
        # dp = {}

        # def helper(starter):
        #     if starter >= len(nums) - 1:
        #         if starter == len(nums) - 1:
        #             return nums[starter]
        #         else:
        #             return 0
        #     if starter in dp:
        #         return dp[starter]
        #     for index in range(starter,len(nums)):
        #         total = nums[index]
        #         for house in range(index + 2, len(nums)):
        #             curr_neighbor = helper(house)
        #             if nums[index] + curr_neighbor > total:
        #                 total = nums[index] + curr_neighbor
        #         dp[index] = total
        #     return dp[starter]
       
        # helper(0)
        # return max(dp[0] if 0 in dp else 0, dp[1] if 1 in dp else 0)
        

        #Approach 2
        if len(nums) == 1:
            return nums[0]
        for index in reversed(range(len(nums))):
            if index == len(nums) - 1:
                continue
            nums[index] = max(nums[index] + (nums[index + 2] if index + 2 < len(nums) else 0),nums[index + 1])
        print(nums)
        return max(nums[0],nums[1])

         
