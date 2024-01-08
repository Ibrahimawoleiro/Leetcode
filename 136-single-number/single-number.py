class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #Approach 1
        checker = set()
        for val in nums:
            if val not in checker:
                checker.add(val)
            else:
                checker.remove(val)
        
        return checker.pop()