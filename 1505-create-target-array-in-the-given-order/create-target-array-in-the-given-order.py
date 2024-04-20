class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = []
        for val in range(len(nums)):
            ans.insert(index[val], nums[val])
        return ans