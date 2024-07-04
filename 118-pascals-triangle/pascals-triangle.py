class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        last = [1]
        ans = []
        for j in range(2, numRows+2):
            curr = [0 for num in range(j)]
            for i in range(j):
                if i == 0 or i == j - 1:
                    curr[i] = 1
                else:
                    curr[i] = last[i - 1] + last[i]
            ans.append(last.copy())
            last = curr

        return ans