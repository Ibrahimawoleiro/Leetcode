class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        store = {}
        min_sum = float('inf')

        def helper(c,store):
            if c[0] >= len(matrix) or c[0] < 0 or c[1] >= len(matrix[0]) or c[1] < 0:
                return float('inf')
            if c in store:
                return store[c]
            if c[0] == len(matrix) - 1:
                store[c] = matrix[c[0]][c[1]]
                return matrix[c[0]][c[1]]
            curr = matrix[c[0]][c[1]] + min(min(helper((c[0] + 1, c[1] + 1), store), helper((c[0] + 1, c[1]),store))         , helper((c[0] + 1, c[1] - 1), store) )
            store[c] = curr
            return curr

        for c_i in range(len(matrix[0])):
            curr = helper((0, c_i), store)
            min_sum = min(curr, min_sum)
        return min_sum