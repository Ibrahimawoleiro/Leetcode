class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #c -> Coordiante (row, col)
        store = {}
        def helper(c,store):
            if c[0] >= m or c[1] >= n:
                return 0
            if c in store:
                return store[c]
            
            down = helper((c[0]+ 1, c[1]), store)
            right = helper((c[0], c[1] + 1), store)

            curr = down + right
            if c[0] == m - 1 and c[1] == n - 1:
                 curr += 1
            
            store[c] = curr

            return curr
        
        ans = helper((0,0), store)
        print(ans)
        print(store)
        return ans
