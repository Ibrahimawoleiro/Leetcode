class Solution:
    def recursive(self, triangle, r, c):
        if c < 0 or c > r:
            return float('inf')
        if r == 0 and c == 0:
            return triangle[r][c]
        #Recursive
        left_diagonal = self.recursive(triangle, r - 1, c - 1)
        right_diagonal = self.recursive(triangle, r - 1, c)
        result = triangle[r][c] + min(left_diagonal, right_diagonal)
        return result

    def memoization(self, triangle, r, c, dp):
        if c < 0 or c > r:
            return float('inf')
        if r == 0 and c == 0:
            return triangle[r][c]
        if dp[r][c] != -1:
            return dp[r][c]
        #Recursive
        left_diagonal = self.memoization(triangle, r - 1, c - 1, dp)
        right_diagonal = self.memoization(triangle, r - 1, c, dp)
        result = triangle[r][c] + min(left_diagonal, right_diagonal)
        dp[r][c] = result
        return result
        
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        min_path = float('inf')
        dp = [[-1 for _ in range(len(triangle[index]))] for index in range(len(triangle))]
        for c in range(len(triangle[-1])):
            min_path = min(min_path, self.memoization(triangle, len(triangle) - 1, c, dp))
        return min_path