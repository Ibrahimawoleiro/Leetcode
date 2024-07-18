class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0

        if nums[0] > nums[1]:
            return 0
        
        if nums[-1] > nums[-2]:
            return len(nums) - 1

        l = 0

        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            print(m)
            if nums[m] > nums[m - 1] and nums[m] > nums[m + 1]:
                return m
            elif nums[m] < nums[m + 1]:
                l = m + 1
            else:
                r = m - 1
                
        print('jksdf')
        return 0