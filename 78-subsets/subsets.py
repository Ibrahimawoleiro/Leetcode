class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]

        def helper(curr, i):
            if i >= len(nums):
                return 
            for index in range(i, len(nums)):
                curr.append(nums[index])
                ans.append(curr.copy())
                helper(curr, index + 1)
                curr.pop()
        helper([], 0)
        return ans

            
