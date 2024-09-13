class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            curr_sum = 0
            for val in nums:
                curr_sum += ceil(val / mid)
            if curr_sum <= threshold:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans