class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[right] > nums[right - 1]:
            return right
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1
        return -1