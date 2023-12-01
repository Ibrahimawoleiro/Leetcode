class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sumOfArray = 0
        for number in nums:
            sumOfArray+=number
        sum = int((len(nums) * (len(nums)+1))/2)
        return sum - sumOfArray