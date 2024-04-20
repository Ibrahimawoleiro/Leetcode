class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        b = 0
        e = len(mat[0]) - 1
        total = 0
        for r in mat:
                if b == e:
                    total += r[b]
                    e -= 1
                    b +=1
                else:
                    total += r[b]
                    total += r[e]
                    e -= 1
                    b += 1
        return total
                
                