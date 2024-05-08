class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #curr is an arr of row, col
        #c is a set for checking
        c = set()
        def helper(i, curr):
            if board[curr[0]][curr[1]] != word[i] or (curr[0],curr[1]) in c:
                return
            if i == len(word) - 1:
                return True
            c.add((curr[0], curr[1]))
            
            if curr[0] > 0:
                if helper(i+1, [curr[0] - 1, curr[1]]):
                    return True
            if curr[0] < len(board) - 1:
                if helper(i + 1, [curr[0] + 1, curr[1]]):
                    return True
            if curr[1] > 0:
                if helper(i + 1, [curr[0], curr[1] - 1]):
                    return True
            if curr[1] < len(board[0]) - 1:
                if helper(i + 1, [curr[0], curr[1] + 1]):
                    return True
            c.remove((curr[0], curr[1]))
              
        for r_index in range(len(board)):
            for c_index in range(len(board[0])):
                    if board[r_index][c_index] == word[0]:
                        if helper(0, [r_index,c_index]):
                            return True
        return False