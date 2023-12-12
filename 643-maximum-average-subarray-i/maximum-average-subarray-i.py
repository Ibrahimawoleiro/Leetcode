class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # #Approach1
        # nums_pointer = 0
        # max_average = -10 ** 6
        # if len(nums) == 1:
        #     return nums[0]
        # while(nums_pointer + k-1 < len(nums)):
        #     i = nums_pointer
        #     sum = 0
        #     while(i < nums_pointer + k):
  
        #         sum += nums[i]
        #         i+=1
        #     if sum/k > max_average:
        #         max_average = sum/k
        #     nums_pointer+=1
        
        # return max_average

        #Appraoch2
        nums_pointer = 0
        max_average = -10 ** 6
        sum = 0
        end = nums_pointer + k - 1
        while(end < len(nums)):
            if nums_pointer == 0:
                i = 0
                while(i <= end):
                    sum+=nums[i]
                    i+=1 
                max_average = sum/k
            else:
                sum -= nums[nums_pointer - 1]
                sum += nums[end]
                if sum / k > max_average:
                    max_average = sum / k

            nums_pointer += 1
            end += 1

        return max_average   