class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        td = len(grid)
        lr = len(grid[0])
        store = {}
        def helper(c, store):
            if c[0] >= td or c[1] >= lr:
                return float('inf')
            if c in store:
                return store[c]
            right = helper((c[0], c[1] + 1), store)
            print(right,'dfghjkl;')
            down  = helper((c[0] + 1, c[1]), store)
            curr = 0
            if c[0] == td - 1 and c[1] == lr - 1:
                curr = grid[c[0]][c[1]]
            else:
                curr = grid[c[0]][c[1]] + min(right, down)
            print(curr)
            store[c] = curr

            return curr
        
        ans =  helper((0,0), store)
        print(store)
        return ans 