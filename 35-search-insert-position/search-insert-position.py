class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                ans = mid
                right = mid - 1
            else:
                ans = mid
                left = mid + 1

        return ans if nums[ans] > target else ans + 1

