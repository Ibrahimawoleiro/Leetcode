class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Approach1

        for index in range(len(nums)):
            for right_index in range(index+1,len(nums)):
                if nums[index] + nums[right_index] == target:
                    return [index, right_index]
