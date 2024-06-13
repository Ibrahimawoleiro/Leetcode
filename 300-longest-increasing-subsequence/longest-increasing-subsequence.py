class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        arr = [1 for num in nums]

        for j in range(len(nums)):
            i = j
            while i >= 0:
                if nums[i] < nums[j] and arr[i] + 1 > arr[j]:
                    arr[j] = arr[i] + 1
                i -= 1

        return max(arr)