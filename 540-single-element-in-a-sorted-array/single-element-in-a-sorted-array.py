class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        if n == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[right] != nums[right - 1]:
            return nums[right]
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid] 
            elif (nums[mid] == nums[mid + 1] and mid % 2 == 0) or (nums[mid] == nums[mid - 1] and mid % 2 == 1): 
                left = mid + 1
            else:
                right = mid - 1
        return -1