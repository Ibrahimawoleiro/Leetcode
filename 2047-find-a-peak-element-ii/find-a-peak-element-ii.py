class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        
        current_row = 0
        current_col = len(mat[0]) - 1

        def isPeak(row, col, current_val):

            upper_neighbor = mat[row - 1][col] if row > 0 else -1
            bottom_neighbor = mat[row + 1][col] if row < len(mat) - 1 else -1
            left_neighbor = mat[row][col - 1] if col > 0 else -1
            right_neighbor = mat[row][col + 1] if col < len(mat[0]) - 1 else -1

            if current_val > upper_neighbor and current_val > bottom_neighbor and current_val > left_neighbor and current_val > right_neighbor: 

                return True

            return False

        def max_neighbor(row, col):

            current = mat[row][col]

            upper_neighbor = mat[row - 1][col] if row > 0 else -1
            bottom_neighbor = mat[row + 1][col] if row < len(mat) - 1 else -1
            left_neighbor = mat[row][col - 1] if col > 0 else -1
            right_neighbor = mat[row][col + 1] if col < len(mat[0]) - 1 else -1

            max_sibling = max(upper_neighbor, max(bottom_neighbor, max(left_neighbor, right_neighbor)))

            if max_sibling == upper_neighbor:
                return [row - 1,col]

            elif max_sibling == bottom_neighbor:
                return [row + 1,col]

            elif max_sibling == left_neighbor:
                return [row,col - 1]

            else:
                return [row,col + 1]




        while current_row > -1 and current_row < len(mat) and current_col > -1 and current_col < len(mat[0]):

            current_value = mat[current_row][current_col]

            if isPeak(current_row, current_col, current_value):
                print(current_row, current_col)
                return [current_row,current_col]

            next_position = max_neighbor(current_row, current_col)

            current_row = next_position[0]
            current_col = next_position[1]

        return [-1,-1]

            
