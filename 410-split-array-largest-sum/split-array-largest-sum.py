class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        if k > len(nums):
                
            return -1
                
        lowest_allocation = max(nums)
        
        highest_allocation = sum(nums)
        
        best_answer = float('inf')
        
        while lowest_allocation <= highest_allocation:
            
            curr_sum = 0
                
            current_allocation = (lowest_allocation + highest_allocation) // 2
                
            students = 1
                
            for val in nums:
                
                if curr_sum + val <= current_allocation:
                            
                        curr_sum += val
                
                else:
                    
                    curr_sum = val
                    
                    students += 1
                    
            # print(lowest_allocation, students)
            
            if students <= k:
                    
                best_answer = min(best_answer,current_allocation)
                    
                highest_allocation = current_allocation - 1
                    
                    
            elif students < k:
                
                highest_allocation = current_allocation - 1
                
            else:
                
                lowest_allocation = current_allocation + 1
                
        return best_answer if best_answer != float('inf') else -1