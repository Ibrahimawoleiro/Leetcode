class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # #Approach 1
        # for index in range(len(nums)):
        #     for checker_index in range(len(nums)):
        #         if(index == checker_index):
        #             continue
        #         if nums[index] == nums[checker_index]:
        #             return True
            
        # return False

        #Approach 2

        nums.sort()
        print(nums)
        for index in range(len(nums)):
            if index == 0:
                continue
            if nums[index] == nums[index - 1]:
                return True
        
        return False
