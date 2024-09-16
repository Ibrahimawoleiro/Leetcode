class Solution:
    def recursive(self,r, c, m, n):
        if r < 0 or c < 0 or r >= m or c >= n:
            return 0
        if r == 0 and c == 0:
            return 1
        else:
            return self.recursive(r - 1, c, m , n) + self.recursive(r, c - 1, m, n)
    def memoized(self,r, c, m, n, dp):
        if r < 0 or c < 0 or r >= m or c >= n:
            return 0
        if r == 0 and c == 0:
            return 1
        if dp[r][c] != -1:
            return dp[r][c]
        else:
            dp[r][c] = self.memoized(r - 1, c, m , n, dp) + self.memoized(r, c - 1, m, n, dp)
        return dp[r][c]
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return self.memoized(m - 1, n - 1, m, n, dp)