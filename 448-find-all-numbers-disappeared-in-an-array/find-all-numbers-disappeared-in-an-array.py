class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        dictionary = {}
        for index in range(len(nums)):
            dictionary[index+1] = 0
        
        for number in nums:
            dictionary[number] = 1

        for key in dictionary:
            if(dictionary[key] == 0 and key != 0):
                result.append(key)

        return result
        