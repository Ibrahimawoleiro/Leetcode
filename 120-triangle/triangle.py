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

    def tabulation(self, triangle):
        dp = [[-1 for _ in range(len(triangle[index]))] for index in range(len(triangle))]
        for r in range(len(triangle)):
            for c in range(len(triangle[r])):
                if r == 0 and c == 0:
                    dp[r][c] = triangle[r][c]
                else:
                    left_diagonal = float('inf')
                    right_diagonal = float('inf')
                    if c - 1 >= 0:
                        left_diagonal = dp[r - 1][c - 1]
                    if c <= r - 1:
                        right_diagonal = dp[r - 1][c]
                    dp[r][c] = triangle[r][c] + min(left_diagonal, right_diagonal)
        ans = float('inf')
        for val in dp[-1]:
            ans = min(ans, val)
        return ans

    def optimized_tabulation(self, triangle):
        prev = [-1 for _ in range(len(triangle[0]))]
        curr = [-1 for _ in range(len(triangle[0]))]
        for r in range(len(triangle)):
            for c in range(len(triangle[r])):
                if r == 0 and c == 0:
                    curr[c] = triangle[r][c]
                else:
                    left_diagonal = float('inf')
                    right_diagonal = float('inf')
                    if c - 1 >= 0:
                        left_diagonal = prev[c - 1]
                    if c <= r - 1:
                        right_diagonal = prev[c]
                    curr[c] = triangle[r][c] + min(left_diagonal, right_diagonal)
            prev = curr
            if r + 1 < len(triangle):
                curr = [-1 for _ in range(len(triangle[r + 1]))]
        ans = float('inf')
        for val in prev:
            ans = min(ans, val)
        return ans
        
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.optimized_tabulation(triangle)