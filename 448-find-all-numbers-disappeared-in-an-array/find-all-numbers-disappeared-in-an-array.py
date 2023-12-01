class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #Approach 1
        # result = []
        # dictionary = {}
        # for index in range(len(nums)):
        #     dictionary[index+1] = 0
        
        # for number in nums:
        #     dictionary[number] = 1

        # for key in dictionary:
        #     if(dictionary[key] == 0 and key != 0):
        #         result.append(key)

        # return result

        #Approach 2
        result = []
        for val in range(len(nums)):
            if(nums[abs(nums[val]) - 1] > 0):
                nums[abs(nums[val]) - 1] *= -1
            
        for val in range(len(nums)):
            if(nums[val] > 0):
                result.append(val+1)

        return result