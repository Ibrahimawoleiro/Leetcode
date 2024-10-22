class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        def isValid(r, c, board):
            #Same column
            row = r
            col = c
            while row >= 0:
                if board[row][col] == 'Q':
                    return False
                row -= 1
            
            row = r
            col = c
            #left diagonal
            while row >= 0 and col >= 0:
                if board[row][col] == 'Q':
                    return False
                row -= 1
                col -= 1

            row = r
            col = c
            #right diagonal
            while row >= 0 and col < n:
                if board[row][col] == 'Q':
                    return False
                row -= 1
                col += 1
            return True


        board = [['.' for _ in range(n)] for _ in range(n)]
        def rec(r, board):
            if r == n:
                curr = []
                for arr in board:
                    curr.append(''.join(arr))
                ans.append(curr)
                return
            for c in range(n):
                if isValid(r, c, board):
                    board[r][c] = 'Q'
                    rec(r + 1, board)
                board[r][c] = '.'

        rec(0, board)
        return ans