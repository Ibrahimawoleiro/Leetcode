class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = int((len(nums) * (len(nums) + 1)) / 2)
        print(sum)
        total = 0

        for num in nums:
            total += num
        
        return sum - total