class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        def recur(s, e):

            if s == e:
                return nums[s]
                
            m = (s + e) // 2

            mid_num = nums[m]

            #Check the middle number to see if it is the unique number
            if nums[m - 1] != mid_num and nums[m + 1] != mid_num:
                return mid_num

            #If we get here, we need to know if we
            #are on the left or right side of the unique number
            start = -1
            if nums[m - 1] == mid_num:
                start = m - 1
            elif nums[m + 1] == mid_num:
                start = m
            
            #We have gotten the index of starting pair
            #Now we check if we are on left or right
            if start % 2 == 0:
                return recur(start + 2, e)
            else:
                return recur(s, start)

        return recur(0,len(nums) - 1)