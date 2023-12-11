class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dictionary = {}
        for val in nums:
            if val in dictionary:
                dictionary[val]+=1
                if len(nums) % 2 == 0 and dictionary[val] >= floor(len(nums) / 2):
                    return val
                elif dictionary[val] == floor((len(nums)+1) / 2):
                    return val
            else:
                dictionary[val] = 1

        print(dictionary)
        return 0