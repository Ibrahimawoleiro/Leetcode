class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        u = set()

        def dfs(p):
            if board[p[0]][p[1]] == 'X' or (p[0], p[1]) in u:
                return 
            u.add((p[0],p[1]))
            if p[0] - 1 >= 0:
                dfs((p[0] - 1, p[1]))
            if p[0] + 1 < len(board):
                dfs((p[0] + 1, p[1]))
            if p[1] - 1 >= 0:
                dfs((p[0], p[1] - 1))
            if p[1] + 1 < len(board[0]):
                dfs((p[0], p[1] + 1))

            

        for c in range(len(board[0])):
            if board[0][c] == 'O':
                dfs((0,c))

        for c in range(len(board[0])):
            if board[len(board) - 1][c] == 'O':
                dfs((len(board) - 1,c)) 

        for r in range(len(board)):
            if board[r][0] == 'O':
                dfs((r,0))
        
        for r in range(len(board)):
            if board[r][len(board[0]) - 1] == 'O':
                dfs((r,len(board[0]) - 1))

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O' and (r, c) not in u:
                    board[r][c] = 'X'