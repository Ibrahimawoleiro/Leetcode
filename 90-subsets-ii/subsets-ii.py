class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen = set()
        seen.add(())
        for index in range(len(nums)):
            self.helper(index, seen, nums, [])

        return list(seen)
        
    def helper(self, index, seen, nums, curr):
        if index >= len(nums):
            return 
        curr.append(nums[index])
        seen.add(tuple(curr))
        if index <= len(nums) - 1:
            for k in range((len(nums) - 1) - index):
                self.helper(index+k+1, seen, nums, curr)
                curr.pop()        
        else:
            curr.pop()