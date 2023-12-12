class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        checker = set()
        boolean = None
        for arr_index in range(len(matrix)):
            for index in range(len(matrix[arr_index])):
                if matrix[arr_index][index] == 0:
                    checker.add(index)
                    boolean = True
            if boolean:
                matrix[arr_index] = [0 for val in range(len(matrix[0]))]
                boolean = None
        
        if checker:
            for val in checker:
                for row_index in range(len(matrix)):
                    matrix[row_index][val] = 0
        