class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()
        i = 0
        j = k -1
        ans = float('inf')
        while(j < len(nums)):
            if nums[j] - nums[i] < ans:
                ans = nums[j] - nums[i]
            
            j += 1
            i += 1
        
        return ans