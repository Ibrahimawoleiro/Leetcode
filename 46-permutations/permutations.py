class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans= []
        def helper(curr):
            if len(nums) == 0:
                ans.append(curr.copy())
                return 
            
            for count in range(len(nums)):
                c = nums.pop(0)
                curr.append(c)
                print("k", len(nums), nums, curr)
                helper(curr)
                nums.append(c)
                curr.pop()
            return ans

        return helper([])

