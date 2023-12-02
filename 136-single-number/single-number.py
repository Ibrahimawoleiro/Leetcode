class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        checker = set()

        for val in nums:
            if val not in checker:
                checker.add(val)
            elif val in checker:
                checker.remove(val)
        
        return checker.pop()