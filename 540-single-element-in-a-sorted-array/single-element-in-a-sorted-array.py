class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        #We have three cases  on where we land on 
            #Case 1: We are on the left side of the single element -> If the current set starts from an even index.
            #Case 2: We are on the right side of the single element -> If the current set starts from an odd index.
            #We are on the single element -> The single element doesn't match what is on the left or right.

        #Edge Cases:
            #Case 1: We are on the right side of the single element -> I need to prevent accessing an index that doesn't exist.
            #Case 2: We are on the element -> I need to prevent accessing an index that doesn't exist.
        
        if len(nums) == 1:
            return nums[0]

        left = 0

        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if mid % 2 == 0 :

                if mid != len(nums) - 1 and nums[mid] == nums[mid + 1]:

                    left = mid + 2

                elif mid != 0 and  nums[mid] == nums[mid - 1]:

                    right = mid - 1

                else:

                    return nums[mid]

            else:

                if  nums[mid] == nums[mid - 1]:

                    left = mid + 1

                elif nums[mid] == nums[mid + 1]:

                    right = mid - 1
                
                else:

                    return nums[mid]

                