import heapq
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        
        nums.sort()
        #[1,2,2,4]
        i = 0
        j = nums[len(nums) - 1] - nums[0]
        m = 10** 10
        while i <= j:

            mid = (i + j) // 2
            count = 0
            k = 1
            while k < len(nums):

                if nums[k] - nums[k - 1] <= mid:
                    count += 1
                    k += 2
                else:
                    k += 1
            if count >= p:
                if mid < m:
                    m = mid
                    j = mid - 1
            else:
                i = mid + 1

        return m