class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        ans = 0

        for val in nums:

            ans = ans ^ val

        return ans