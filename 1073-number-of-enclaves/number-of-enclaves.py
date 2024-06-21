class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(p):
            if grid[p[0]][p[1]] == 0:
                return
            grid[p[0]][p[1]] = 0
            if p[0] - 1 >= 0:
                dfs((p[0] - 1, p[1]))
            if p[0] + 1 < len(grid):
                dfs((p[0] + 1, p[1]))
            if p[1] - 1 >= 0:
                dfs((p[0], p[1] - 1))
            if p[1] + 1 < len(grid[0]):
                dfs((p[0], p[1] + 1))

        for c in range(len(grid[0])):
            if grid[0][c] == 1:
                dfs((0, c))

        for c in range(len(grid[0])):
            if grid[len(grid) - 1][c] == 1:
                dfs((len(grid) - 1, c))

        for r in range(len(grid)):
            if grid[r][0] == 1:
                dfs((r, 0))

        for r in range(len(grid)):
            if grid[r][len(grid[0]) - 1] == 1:
                dfs((r, len(grid[0]) - 1))

        count = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    count += 1

        return count
