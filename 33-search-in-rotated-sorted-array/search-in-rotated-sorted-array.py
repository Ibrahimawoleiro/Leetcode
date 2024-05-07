class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Brute force
        for index in range(len(nums)):
            if nums[index] == target:
                return index
        return -1