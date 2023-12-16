class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # #Approach1
        # max_sum = nums[0]

        # for outer_index in range(len(nums)):
        #     current = 0
        #     for val in range(outer_index, len(nums)):
        #         current+=nums[val]
        #         if current > max_sum:
        #             max_sum = current
                
        # return max_sum

        #Approach2
        overall_max = nums[-1]
        current_sum = 0
        for index in range(len(nums)):
            if nums[index] > current_sum + nums[index]:
                current_sum = nums[index]
                if current_sum > overall_max:
                    overall_max = current_sum
            else:
                current_sum += nums[index]
                if current_sum > overall_max:
                    overall_max = current_sum
        
        return overall_max
            



