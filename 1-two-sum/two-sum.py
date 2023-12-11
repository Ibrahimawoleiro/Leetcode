class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Approach1
        dictionary = {}
        for index in range(len(nums)):
            dictionary[nums[index]] = index
        print(dictionary)
        for index in range(len(nums)):
            if target - nums[index] in dictionary and dictionary[target - nums[index]] != index:
                return [index, dictionary[target - nums[index]]]
