class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for index in range(len(nums)):
            curr = nums[abs(nums[index]) - 1]
            if curr < 0:
                ans.append(abs(nums[index]))
            else:
                nums[abs(nums[index]) - 1] *= -1
        
        return ans