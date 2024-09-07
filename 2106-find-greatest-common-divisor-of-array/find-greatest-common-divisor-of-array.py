class Solution:
    def findGCD(self, nums: List[int]) -> int:
        low = min(nums)
        maxi = max(nums)
        ans = 0
        for val in range(1, low + 1):
            if low % val == 0 and maxi % val == 0:
                ans = val
            
        return ans