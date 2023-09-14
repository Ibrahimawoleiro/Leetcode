class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Create a varible left
        Create a variable right
        Create a variable mid
        
        Now create a while loop that runs as long as left <= right:
        mid = (left + right)/2
        Check the value at mid. If it is the target, return the index of target.
            Else if the number at mid is greater than the target, Then right = mid -1
            Else if the number at mid is less than the target, Then left = mid +1
            
        if number isn't found return left because left will be at the index where the number would have
        been.
        
        
        """
        
        left = 0
        right = len(nums)
        
        while left<=right:
            mid = int((left + right)/2)
            
            if mid >= len(nums):
                return mid
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
                
        return left