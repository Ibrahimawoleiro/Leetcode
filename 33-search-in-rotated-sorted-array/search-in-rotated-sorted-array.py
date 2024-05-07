class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # #Brute force
        # for index in range(len(nums)):
        #     if nums[index] == target:
        #         return index
        # return -1

        #Cases: 
        l = 0
        r = len(nums) - 1

        while(l <= r):
            if nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            if target > nums[l]:
                r -= 1
            elif target < nums[l]:
                l += 1
        return -1 
