class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def helper(save, curr,index):
            if curr not in seen and board[curr[0]][curr[1]] == word[index]:
                if index == len(word) - 1:
                    return True
                save.add(curr)
                if curr[0] > 0:
                    if helper(save,(curr[0] - 1,curr[1]),index + 1):
                        return True
                if curr[0] < len(board) - 1:
                    if helper(save,(curr[0] + 1,curr[1]),index + 1):
                        return True
                if curr[1] > 0:
                    if helper(save,(curr[0],curr[1] - 1),index + 1):
                        return True
                if curr[1] < len(board[0]) - 1:
                    if helper(save,(curr[0],curr[1] + 1),index + 1):
                        return True
                save.remove(curr)
            else:
                return False

        seen = set()
        for row in range(len(board)):
            for col in range(len(board[0])):

                if word[0] == board[row][col]:
                    if helper(seen,(row,col),0):
                        return True

        return False

        