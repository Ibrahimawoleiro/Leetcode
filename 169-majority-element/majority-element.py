class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        curr_count = 1
        curr_number = -1

        for number in nums:
            if number != curr_number:
                curr_count -= 1
                if curr_count == 0:
                    curr_count = 1
                    curr_number = number
            else:
                curr_count += 1
        
        return curr_number