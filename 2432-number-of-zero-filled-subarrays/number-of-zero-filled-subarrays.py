class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        total = 0
        curr = 0

        for index in range(len(nums)):
            if nums[index] == 0:
                curr += 1
            else:
                total += (curr * (curr + 1)) // 2
                curr = 0
        if curr > 0:
            total += (curr * (curr + 1)) // 2
            curr = 0
        return total
