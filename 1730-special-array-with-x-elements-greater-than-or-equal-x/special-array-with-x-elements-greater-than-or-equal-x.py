class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for num in range(1,len(nums) + 1):
            count = 0
            for val in nums:
                if val >= num:
                    count += 1

            if count == num:
                return num
            
        return -1
