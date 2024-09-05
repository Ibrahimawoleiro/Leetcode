class Solution:
    
    def jump(self, nums: List[int]) -> int:
        # def recursive(nums,index, jumps):
        #     if index >= len(nums) - 1:
        #         return jumps
        #     if nums[index] == 0:
        #         return float('inf')
        #     mini = float('inf')
        #     for option in range(1, nums[index] + 1):
        #         mini = min(mini, recursive(nums, index + option, jumps + 1))
        #     return mini

        # dp = [[-1 for _ in range(len(nums))] for _ in range(len(nums))]
        # def memoized(nums,index, jumps, dp):
        #     if index >= len(nums) - 1:
        #         return jumps
        #     if nums[index] == 0:
        #         return float('inf')
        #     if dp[index][jumps] != -1:
        #         return dp[index][jumps]
        #     mini = float('inf')
        #     for option in range(1, nums[index] + 1):
        #         mini = min(mini, memoized(nums, index + option, jumps + 1, dp))
        #     dp[index][jumps] = mini
        #     return mini
            
        def greedy(nums):
            jumps = 0
            l = 0
            r = 0
            while r < len(nums) - 1:
                jumps += 1
                maxi = l
                for i in range(l, r + 1):
                    if i >= len(nums):
                        break
                    maxi = max(maxi, nums[i] + i)
                l = r + 1
                r = maxi 
            return jumps
        return greedy(nums)