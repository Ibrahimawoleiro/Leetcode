class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Create a variable called island_count
        Create a variable called max_island_count
        Create a for loop that runs n times
            Create another for loop that runs n times in the first for loop
                Start the logic from [0,0].
                Check if current node is a land by checking if the value is 1.
                    if yes, this means that the current node has not been visited
                        Now we use a dfs on this node to check for its neighbors to see if this node is                         an island on its own or it spreads.
                        If neighbor hasn't been seen, push it on to the stack using a list of the index 
                        in [x,y] where x is the row and y is the column
                            Once we visit a node, we mark the current as visited by changing val to 5
                            Edge cases: 
                               The top is less than the 0 :In this case,we skip checking the top
                               The bottom is greater than the m: We skip in this case
                               The left is less than the 0: We skip in this case
                               The right is greater than n: We skip in this case
        """
        max_island = 0
        direction = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    direction.append([row,col])
                    grid[row][col]=5
                    count = 0
        
                    while(direction):
                        curr = direction.pop()
                        count +=1
                        
                        if count > max_island:
                            max_island = count
                        
                        if curr[0]-1>=0:
                            if grid[curr[0]-1][curr[1]] == 1:
                                direction.append([curr[0]-1,curr[1]])
                                grid[curr[0]-1][curr[1]]=5
                        if curr[0]+1<len(grid):
                            if grid[curr[0]+1][curr[1]] == 1:
                                direction.append([curr[0]+1,curr[1]])
                                grid[curr[0]+1][curr[1]]=5
                        if curr[1]-1>=0:
                            if grid[curr[0]][curr[1]-1] == 1:
                                direction.append([curr[0],curr[1]-1])
                                grid[curr[0]][curr[1]-1]=5

                        if curr[1]+1<len(grid[0]):
                            if grid[curr[0]][curr[1]+1] == 1:
                                direction.append([curr[0],curr[1]+1])
                                grid[curr[0]][curr[1]+1]=5

        return max_island