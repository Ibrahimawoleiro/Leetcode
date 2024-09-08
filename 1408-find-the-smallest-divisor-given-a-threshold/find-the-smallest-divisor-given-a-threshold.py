class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = sum(nums)
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            total = 0
            for val in nums:
                total += int(ceil(val / mid))
            if total <= threshold:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans