class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = [[0 for val in range(len(matrix))] for val in range(len(matrix[0]))]
        ans_r = 0
        ans_c = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                ans[ans_r][ans_c] = matrix[r][c]
                ans_r += 1
                if ans_r >= len(ans):
                    ans_c +=1
                    ans_r = 0
        
        return ans
