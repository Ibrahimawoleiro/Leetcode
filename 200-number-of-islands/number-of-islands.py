class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #Create a counter
        #Loop through the 2D array 
        #When you find an island, increase counter
            #Find all the land connected to current island and mark them as seen 
        #return the counter

        counter = 0
        for r_index in range(len(grid)):
            for c_index in range(len(grid[0])):
                if grid[r_index][c_index] == "1":
                    counter += 1
                    stack = [[r_index, c_index]]
                    while(stack):
                        curr = stack.pop()
                        grid[curr[0]][curr[1]] = 5
                        if curr[0] > 0 and grid[curr[0] - 1] [curr[1]] == '1':
                            stack.append([curr[0] - 1, curr[1]])
                        if curr[0] < len(grid) - 1 and grid[curr[0] + 1][curr[1]] == '1':
                            stack.append([curr[0] + 1, curr[1]])
                        if curr[1] > 0 and grid[curr[0]][curr[1] - 1] == '1':
                            stack.append([curr[0],curr[1] - 1])
                        if curr[1] < len(grid[0]) - 1 and grid[curr[0]][curr[1] + 1] == '1':
                            stack.append([curr[0],curr[1] + 1])
        
        return counter
                        
