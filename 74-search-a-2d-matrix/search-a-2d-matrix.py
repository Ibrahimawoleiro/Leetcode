class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        col_length = len(matrix)
        row_length = len(matrix[0])

        start = 0
        end = col_length * row_length - 1

        while start <= end:

            mid = (start + end) // 2

            row = mid // row_length

            col = mid % row_length

            if matrix[row][col] == target:

                return True

            elif matrix[row][col] > target:

                end = mid - 1

            else:

                start = mid + 1

        return False

