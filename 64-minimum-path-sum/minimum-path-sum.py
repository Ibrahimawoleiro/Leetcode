class Solution:
    def recursive(self,grid, r , c):
        if r < 0 or c < 0:
            return float('inf')
        if r == 0 and c == 0:
            return grid[0][0]
        #Recursive
        return grid[r][c] + min(self.recursive(grid, r - 1,c), self.recursive(grid, r, c - 1))
    
    def memoized(self,grid, r , c, dp):
        if r < 0 or c < 0:
            return float('inf')
        if r == 0 and c == 0:
            return grid[0][0]
        if dp[r][c] != -1:
            return dp[r][c]
        #Recursive
        dp[r][c] = grid[r][c] + min(self.memoized(grid, r - 1,c,dp), self.memoized(grid, r, c - 1,dp))
        return dp[r][c]

    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        return self.memoized(grid, len(grid) - 1, len(grid[0]) - 1, dp)