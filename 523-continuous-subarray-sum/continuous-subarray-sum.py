class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        total = 0
        store = {0:-1}

        for index in range(len(nums)):
            total += nums[index]
            remainder = total % k
            if remainder in store:

                if index - store[remainder] >= 2:
                    return True
                
            else:
                store[remainder] = index
        
        return False