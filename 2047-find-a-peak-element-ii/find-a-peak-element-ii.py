class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        low = 0
        high = len(mat) - 1
        while low <= high:
            mid = (low + high) // 2
            max_col = 0
            val = mat[mid][0]
            for index in range(len(mat[0])):
                if mat[mid][index] > val:
                    val = mat[mid][index]
                    max_col = index
            top = True
            bottom = True
            if mid - 1 >= 0 and mat[mid - 1][max_col] > mat[mid][max_col]:
                high = mid - 1
                top = False
            if mid + 1 < len(mat) and mat[mid + 1][max_col] > mat[mid][max_col]:
                low = mid + 1
                bottom = False
            if top and bottom:
                return [mid, max_col]

        return [-1, -1]

