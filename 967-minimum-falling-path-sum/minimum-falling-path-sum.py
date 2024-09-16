class Solution:
    def recursive(self, matrix, r, c):
        if c < 0 or c >= len(matrix[0]):
            return float('inf')
        if r == 0:
            return matrix[r][c]
        #Recursive
        left = float('inf')
        middle = float('inf')
        right = float('inf')
        left = self.recursive(matrix, r - 1, c - 1)
        middle = self.recursive(matrix, r - 1, c)
        right = self.recursive(matrix, r - 1, c + 1)
        result = matrix[r][c] + min(left, middle, right)
        return result

    def memoized(self, matrix, r, c, dp):
        if c < 0 or c >= len(matrix[0]):
            return float('inf')
        if r == 0:
            return matrix[r][c]
        if dp[r][c] != -1:
            return dp[r][c]
        #Recursive
        left = self.memoized(matrix, r - 1, c - 1, dp)
        middle = self.memoized(matrix, r - 1, c, dp)
        right = self.memoized(matrix, r - 1, c + 1, dp)
        result = matrix[r][c] + min(left, middle, right)
        dp[r][c] =  result
        return result
    
    def tabulation(self, matrix):
        dp = [[-1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r == 0:
                    dp[r][c] = matrix[r][c]
                else:
                    left = float('inf')
                    middle = float('inf')
                    right = float('inf')
                    if c - 1 >= 0:
                        left = matrix[r][c] + dp[r - 1][c - 1]
                    middle = matrix[r][c] + dp[r - 1][c]
                    if c + 1 < len(matrix[0]):
                        right = matrix[r][c] + dp[r - 1][c + 1]
                    dp[r][c] = min(left, middle, right)
        ans = float('inf')
        for val in dp[-1]:
            ans = min(ans , val)
        return ans

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        return self.tabulation(matrix)