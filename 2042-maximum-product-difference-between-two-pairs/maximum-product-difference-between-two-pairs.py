class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        arr = sorted(nums)
        return (arr[-1] * arr[-2]) - (arr[0] * arr[1])