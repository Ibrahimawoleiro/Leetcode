import queue
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ans = [[0 for num in range(len(mat[0]))] for val in range(len(mat))]
        seen = set()
        q = queue.Queue()
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0:
                    q.put((r,c))
                    seen.add((r,c))
        q.put(None)
        d = 0
        while(not q.empty()):
            curr = q.get()
            if curr:
                r = curr[0]
                c = curr[1]
                ans[r][c] = d
                if r - 1 >= 0 and (r - 1, c) not in seen:
                    q.put((r-1,c))
                    seen.add((r - 1, c))
                if r + 1 < len(ans) and (r + 1, c) not in seen:
                    q.put((r + 1, c))
                    seen.add((r + 1, c))
                if c - 1 >= 0 and (r, c - 1) not in seen:
                    q.put((r, c - 1))
                    seen.add((r, c - 1))
                if c + 1 < len(ans[0]) and (r, c + 1) not in seen:
                    q.put((r, c + 1))
                    seen.add((r, c + 1))
            else:
                # print(seen)
                if not q.empty():
                    d += 1
                    # print(d)
                    q.put(None)
        return ans