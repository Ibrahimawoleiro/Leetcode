class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        checker = set()

        for val in nums:
            if val in checker:
                return val
            checker.add(val) 
        