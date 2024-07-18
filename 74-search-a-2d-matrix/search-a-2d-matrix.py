class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        def findRow(top, bottom):

            while top <= bottom:
                mid = (top + bottom) // 2
                if mid + 1 == len(matrix):
                    return len(matrix) - 1
                else:
                    if target < matrix[mid + 1][0] and target >= matrix[mid][0]:
                        return mid
                    else:
                        if target < matrix[mid][0]:
                            bottom = mid - 1
                        else:
                            top = mid + 1

            return -1

        index = findRow(0, len(matrix) - 1)

        left = 0

        right = len(matrix[0]) - 1

        while left <= right:

            mid = (left + right) // 2

            if matrix[index][mid] ==  target:
                return True
            
            if matrix[index][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
