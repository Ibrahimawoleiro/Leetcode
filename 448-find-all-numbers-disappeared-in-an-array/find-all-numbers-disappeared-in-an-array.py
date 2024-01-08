class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #Approach 1
        checker = set()

        for val in nums:
             checker.add(val)

        result = []
        for number in range(1,len(nums)+1):
            if number not in checker:
                result.append(number)
        
        return result
            

        