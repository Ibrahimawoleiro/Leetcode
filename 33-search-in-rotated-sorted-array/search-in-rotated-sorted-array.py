class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        def binary_search(start, end):
            left = start
            right = end
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        def find(start, end):
            if start >= end:
                if nums[start] == target:
                    return start
                return -1
            middle = (start + end) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] < nums[end] and nums[start] > nums[middle]:
                result = binary_search(middle, end)
                if result > -1:
                    return result
                return find(start, middle - 1)
            elif nums[middle] > nums[start] and nums[middle] > nums[end]:
                result = binary_search(start, middle - 1)
                if  result > -1:
                    return result
                return find(middle + 1, end)
            else:
                result_l = find(start, middle - 1)
                if result_l > -1:
                    return result_l
                result_r = find(middle + 1, end)
                return result_r
        return find(0, n - 1)