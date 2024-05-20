

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        # If the total sum is odd, it's not possible to partition it into two equal subsets
        if total % 2 == 1:
            return False

        target = total // 2

        # Initialize a DP array where dp[j] indicates if a subset with sum j can be formed
        dp = [False] * (target + 1)
        dp[0] = True

        # Iterate through the numbers in the array
        for num in nums:
            # Update the DP array from back to front
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[target]
