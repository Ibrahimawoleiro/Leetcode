class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        j = k - 1
        sum_subarr = sum(nums[0:k])
        max_subarr = sum_subarr / k
        while j < len(nums):
            if j == k - 1:
                j+=1
                sum_subarr -= nums[i]
                i+=1
                continue
            sum_subarr += nums[j]
            curr_subarr_avg = sum_subarr / k
            if curr_subarr_avg > max_subarr:
                max_subarr = curr_subarr_avg
            sum_subarr -= nums[i]
            i+=1
            j+=1
            
        
        return max_subarr