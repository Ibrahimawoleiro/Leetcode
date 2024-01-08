class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # #Approach 1
        # checker = set()

        # for val in nums:
        #      checker.add(val)

        # result = []
        # for number in range(1,len(nums)+1):
        #     if number not in checker:
        #         result.append(number)
        
        # return result

        #Approach 2

        for index in range(len(nums)):
            if nums[abs(nums[index]) - 1] > 0:
                nums[abs(nums[index]) - 1] *= -1

        result = []

        for index in range(len(nums)):
            if nums[index] > 0:
                result.append(index+1)
        
        return result
            

        