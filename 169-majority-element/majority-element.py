class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # #Approach1
        # if len(nums) == 1:
        #     return nums[0]
        # dictionary = {}
        # for val in nums:
        #     if val in dictionary:
        #         dictionary[val]+=1
        #         if len(nums) % 2 == 0 and dictionary[val] >= floor(len(nums) / 2):
        #             return val
        #         elif dictionary[val] == floor((len(nums)+1) / 2):
        #             return val
        #     else:
        #         dictionary[val] = 1

        # print(dictionary)
        # return 0

        #Approach2
        majority = None
        count = 0

        for val in nums:
            if count == 0:
                majority = val
                count = 1
                continue
            if val == majority:
                count+=1
            else:
                count -=1

        return majority