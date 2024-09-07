class Solution:
    def findMin(self, nums: List[int]) -> int:

           #Identify the minimum side and return the minimum
           #Identify the unsorted side and call the recursive case on it
        def rec(s, e):
            if s > e:
                return 10000
            if s == e:
                return nums[s]
            mid = (s + e) // 2
            if nums[mid] > nums[s]:
                return min(nums[s], rec(mid + 1, e))
            elif nums[mid] < nums[e]:
                return min(nums[mid], rec(s, mid - 1))
            else:
                return min(rec(s, mid), rec(mid+ 1, e))
        return rec(0, len(nums) - 1)
