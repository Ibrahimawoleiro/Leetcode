class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        zero_count = 0
        current_max_window = 0
        highest_max_window = 0
        
        while(right < len(nums)):
            if nums[right] == 1 or (nums[right] == 0 and zero_count<k):
                if(nums[right]==0):
                    zero_count+=1
                current_max_window +=1
                right+=1
            else:
                if nums[left] == 0:
                    zero_count-=1
                left+=1
                current_max_window-=1
            
            if(current_max_window>highest_max_window):
                highest_max_window = current_max_window
        
        return highest_max_window
                