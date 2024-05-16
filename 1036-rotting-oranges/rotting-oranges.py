import queue
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = queue.Queue()
        #Get the indexes with the rotten tomatoes
        m = 0
        g = 0
        s = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.put((r,c))
                elif grid[r][c] == 1:
                    g += 1
        q.put(None)
       
        while q:
            curr = q.get()
            if curr == None:
                m += 1
                if q.empty():
                    break
                else:
                    q.put(None)
                    continue

            if curr[0] > 0 and grid[curr[0] - 1][curr[1]] == 1:
                s+=1
                grid[curr[0] - 1][curr[1]] = 2
                q.put( (curr[0] - 1, curr[1]) )
            if curr[0] < len(grid) - 1 and grid[curr[0] + 1][curr[1]] == 1:
                s+=1
                grid[curr[0] + 1][curr[1]] = 2
                q.put( (curr[0] + 1, curr[1]) )
            if curr[1] > 0 and grid[curr[0]][curr[1] - 1] == 1:
                s+=1
                grid[curr[0]][curr[1] - 1] = 2
                q.put( (curr[0], curr[1] - 1) )
            if curr[1] < len(grid[0]) - 1 and grid[curr[0]][curr[1] + 1] == 1:
                s+=1
                grid[curr[0]][curr[1] + 1] = 2
                q.put( (curr[0], curr[1] + 1) )

        return m - 1 if s == g else -1
