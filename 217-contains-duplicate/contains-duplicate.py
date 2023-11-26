class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #Approach1
        if len(nums) == 1:
            return False
        #Create a left and right pointer
        left = 0
        right = 1

        #Sort the array
        nums.sort()
        #Loop through the sorted array while checking current to the last seen 
        #if equal, return false 
        #if no false was return, return true
        while(right < len(nums)):
            if(nums[left] == nums[right]):
                return True
            left+=1
            right+=1
        return False