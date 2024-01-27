class Solution:
     def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # #Approach 1
        # ans = [0]

        # def helper(index, total,answer):
        #     if index == len(nums):
        #         if total == target:
        #             answer[0] += 1
        #         return 
        #     helper(index + 1, total + nums[index], answer)
        #     helper(index + 1, total - nums[index], answer)

        # helper(0, 0, ans)

        # return ans[0]

        #Approach 2:
        dp = {}
        def helper(index, total):
            if index == len(nums):
                return 1 if total == target else  0

            if (index,total) in dp:
                return dp[(index,total)] 
            

            curr = helper(index + 1, total + nums[index]) + helper(index + 1, total - nums[index])
            print(curr)
            dp[(index,total)] = curr
            return curr

        return helper(0,0)
         


        
            