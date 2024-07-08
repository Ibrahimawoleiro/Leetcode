class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = matrix
        for r in range(len(self.prefix)):
            for c in range(len(self.prefix[0])):
                if c == 0:
                    continue
                self.prefix[r][c] = self.prefix[r][c - 1] + self.prefix[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for r in range(row1, row2 + 1):
            if col1 > 0:
                total += self.prefix[r][col2] - self.prefix[r][col1 - 1]
            else:
                total += self.prefix[r][col2]
        return total
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)