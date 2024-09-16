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
    
    def tabulation(self, grid):
        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if r == 0 and c == 0:
                    dp[r][c] = grid[0][0]
                else:
                    dp[r][c] = grid[r][c] + min(dp[r - 1][c] if r > 0 else float('inf'), dp[r][c - 1] if c > 0 else float('inf'))
        return dp[len(grid) - 1][len(grid[0]) - 1]
    
    def optimized_tabulation(self, grid):
        prev = [0 for _ in range(len(grid[0]))]
        curr = [0 for _ in range(len(grid[0]))]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if r == 0 and c == 0:
                    curr[c] = grid[0][0]
                else:
                    curr[c] = grid[r][c] + min(prev[c] if r > 0 else float('inf'), curr[c - 1] if c > 0 else float('inf'))
            prev = curr
            curr = [0 for _ in range(len(grid[0]))]
        return prev[len(grid[0]) - 1]
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        return self.optimized_tabulation(grid)