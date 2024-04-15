class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        maximum = 0
        i = 0
        j = 0

        while( j< len(nums)):
            if i == j:
                j+=1
                continue
            
            if nums[j] - nums[i] > 1:
                i+=1
                continue
            
            if nums[j] - nums[i] == 1:
                if maximum < (j - i) + 1:
                    maximum = (j - i) + 1
            
            j+=1
        return maximum