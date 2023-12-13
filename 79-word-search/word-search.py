class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        
        for row_index in range(len(board)):
            for col_index in range(len(board[0])):
                if board[row_index][col_index] == word[0]:
                    seen = set()
                    i = 1
                    print(seen)
                    if self.helper([row_index,col_index, i], seen,board,word):
                        return True
        return False

    def helper(self, curr, seen,board,word):
        if curr[2] == len(word):
            return True
        seen.add((curr[0] , curr[1]))
        if(curr[0] - 1 >= 0 and (curr[0] - 1  , curr[1]) not in seen):
            if board[curr[0] - 1][curr[1]] == word[curr[2]]:
                if self.helper([curr[0] - 1  , curr[1], curr[2] + 1],seen,board,word):
                    return True

        if(curr[0] + 1 < len(board) and (curr[0] + 1  , curr[1]) not in seen):
            if board[curr[0] + 1][curr[1]] == word[curr[2]]:
                if self.helper([curr[0] + 1  , curr[1] , curr[2] + 1],seen,board,word):
                    return True
                

        if(curr[1] + 1 < len(board[0]) and (curr[0] , curr[1] + 1) not in seen):
            if board[curr[0]][curr[1] + 1] == word[curr[2]]:
                if self.helper([curr[0] , curr[1] + 1, curr[2] + 1],seen,board,word):
                    return True

        if(curr[1] - 1 >= 0 and (curr[0] , curr[1] - 1) not in seen):
            if board[curr[0]][curr[1] - 1] == word[curr[2]]:
                if self.helper([curr[0] , curr[1] - 1, curr[2] + 1],seen,board,word):
                    return True

        seen.remove((curr[0] , curr[1]))