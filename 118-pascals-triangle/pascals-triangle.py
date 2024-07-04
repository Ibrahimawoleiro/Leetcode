class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        last = [1]
        if numRows == 1:
            return [last]
        ans = []
        for j in range(2, numRows+1):
            curr = [0 for num in range(j)]
            for i in range(j):
                if i == 0 or i == j - 1:
                    curr[i] = 1
                else:
                    curr[i] = last[i - 1] + last[i]
            if j == 2:
                ans.append(last.copy())
                ans.append(curr.copy())
            else:
                ans.append(curr.copy())
            last = curr

        return ans