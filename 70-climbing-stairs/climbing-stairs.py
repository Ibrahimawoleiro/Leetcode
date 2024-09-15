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
    def tabulation(self,n):
        dp = [-1 for _ in range(n + 1)]
        for i in range(n + 1):
            if i == 0 or i == 1:
                dp[i] = 1
            else:
                dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
    def optimized_tabulation(self, n):
        prev = curr = 1 
        for index in range(2, n + 1):
            temp = curr + prev
            prev = curr
            curr = temp
        return curr
    def climbStairs(self, n: int) -> int:
        return self.optimized_tabulation(n)