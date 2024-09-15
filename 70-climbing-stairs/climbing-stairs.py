class Solution:
    def recursive(self,n):
        if n == 1 or n == 0:
            return 1
        return self.recursive(n - 1) + self.recursive(n - 2)
    
    def memoized(self, n, dp):
        if n == 1 or n == 0:
            return 1
        if dp[n] != -1:
            return dp[n]
        dp[n] = self.memoized(n - 1, dp) + self.memoized(n - 2, dp)
        return dp[n]

    def climbStairs(self, n: int) -> int:
        dp = [-1 for _ in range(n + 1)]
        return self.memoized(n, dp)