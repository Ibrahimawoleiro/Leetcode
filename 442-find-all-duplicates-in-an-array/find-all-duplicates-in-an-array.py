class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        checker = set()
        for val in nums:
            if val in checker:
                result.append(val)
                continue
            checker.add(val)

        return result