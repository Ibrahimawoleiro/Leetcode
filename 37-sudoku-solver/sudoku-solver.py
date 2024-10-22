class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def can_place(val, r, c):
            for i in range(9):
                if board[i][c] == str(val):
                    return False
                if board[r][i] == str(val):
                    return False
                if board[3 * (r // 3) + (i // 3)][3 * (c // 3) + (i % 3)] == str(val):
                    return False
            return True
        def rec(board):
            empty_seen  = False
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        empty_seen = True
                        for val in range(1, 10):
                            if can_place(val, r, c):
                                board[r][c] = str(val)
                                if rec(board):
                                    return True
                                board[r][c] = '.'
                        return False
            if not empty_seen:
                return True
            return False
        
        return rec(board)
        