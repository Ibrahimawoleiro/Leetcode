class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0 for num in range(2*len(nums))]

        for index in range(len(nums)):
            ans[index] = nums[index]
            ans[len(nums) + index] = nums[index]

        return ans