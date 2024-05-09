class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        ans.add(())
        def helper(curr, i):
            if i >= len(nums):
                return 
            for index in range(i ,len(nums)):
                curr.append(nums[index])
                ans.add(tuple(curr.copy()))
                helper(curr, index + 1)
                curr.pop()

        helper([], 0)
        return list(ans)