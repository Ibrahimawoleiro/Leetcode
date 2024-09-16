class Solution:
    # def recursive(self,r, c, m, n):
    #     if r < 0 or c < 0:
    #         return 0
    #     if r == 0 and c == 0:
    #         return 1
    #     else:
    #         return self.recursive(r - 1, c, m , n) + self.recursive(r, c - 1, m, n)

    # def memoized(self,r, c, m, n, dp):
    #     if r < 0 or c < 0:
    #         return 0
    #     if r == 0 and c == 0:
    #         return 1
    #     if dp[r][c] != -1:
    #         return dp[r][c]
    #     else:
    #         dp[r][c] = self.memoized(r - 1, c, m , n, dp) + self.memoized(r, c - 1, m, n, dp)
    #     return dp[r][c]
    
    def tabulation(self,m,n):
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        for row in range(m):
            for col in range(n):
                if row == 0 and col == 0:
                    dp[row][col] = 1
                else:
                    up = 0
                    left = 0
                    if row - 1 >= 0:
                        up = dp[row - 1][col]
                    if col - 1 >= 0:
                        left = dp[row][col - 1]
                    dp[row][col] = up + left
        return dp[m - 1][n - 1]
    
    def optimized_tabulation(self, m,n):
        pass

    def uniquePaths(self, m: int, n: int) -> int:
        return self.tabulation(m, n)