class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Identify the minimum side and return the minimum
        #Identify the unsorted side and call the recursive case on it
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        def rec(start, end):
            if start >= end:
                if start == end:
                    return nums[start]
                return 10000
            mid = (start + end) // 2
            if nums[mid] > nums[start]:
                return min(nums[start], rec(mid + 1, end))
            elif nums[mid] < nums[end]:
                return min(nums[mid], rec(start , mid - 1))
            else:
                return min(rec(start, mid - 1), rec(mid + 1 , end))
        result = rec(0 , n - 1)
        return result 