class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        i = 0
        j = 1
        while(j < len(nums)):
            if nums[i] == nums[j]:
                i+=1
                j+=1
            elif nums[i] < nums[j]:
                i+=1
                j+=1
                while(j < len(nums)):
                    if nums[i] > nums[j]:
                        return False
                    i+=1
                    j+=1
            else:
                i+=1
                j+=1
                while(j < len(nums)):
                    if nums[i] < nums[j]:
                        return False
                    i+=1
                    j+=1

        return True