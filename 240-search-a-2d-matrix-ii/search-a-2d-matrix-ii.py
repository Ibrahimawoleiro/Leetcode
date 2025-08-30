class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        current_row = 0

        current_column = len(matrix[0]) - 1

        while current_row > -1 and current_row < len(matrix) and current_column > -1 and current_column < len(matrix[0]):

            current_value = matrix[current_row][current_column]

            if current_value == target:

                return True

            elif current_value > target:

                current_column -= 1

            else:

                current_row += 1

        return False