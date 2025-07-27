class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        left = 1
        right = max(nums)

        ans = min(nums)

        while left <= right:

            mid = (left + right) // 2

            total = 0

            for val in nums:

                total += math.ceil(val / mid)

            if total <= threshold:

                ans = mid

                right = mid - 1

            else:

                left = mid + 1

        return ans