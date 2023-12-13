class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #Approach1
        x = len(matrix[0]) - 1
        y = 0
        two_d = [[0 for val in range(len(matrix[0]))] for val in range(len(matrix))]
        for row in matrix:
            for col in row:
                two_d[y][x] = col
                y+=1
            x-=1
            y=0
        for row in range(len(two_d)):
            matrix[row] = two_d[row]
                