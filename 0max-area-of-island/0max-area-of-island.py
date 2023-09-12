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
        
        island_count = 0
        max_island_count = 0
        #seen = set()
        for num in range(len(grid)):
            for val in range(len(grid[0])):
                #print(val)
                island_count = 0
                if grid[num][val] == 1:
                    stack = []
                    stack.append([num,val])
                    while stack:
                        #print(stack)
                        curr = stack.pop()
                        #print(stack)
                        if grid[curr[0]][curr[1]] == 1:
                            island_count+=1
                            grid[curr[0]][curr[1]] = 5
                            #print(grid[curr[0]][curr[1]], "jj")
                            if curr[0] - 1 >= 0:
                                if grid[curr[0]-1][curr[1]] == 1:
                                    stack.append([curr[0]-1,curr[1]])
                            if curr[1] - 1 >= 0:
                                if grid[curr[0]][curr[1]-1] == 1:
                                    stack.append([curr[0],curr[1]-1])
                            if curr[0] + 1 < len(grid):
                                if grid[curr[0]+1][curr[1]] == 1:
                                    stack.append([curr[0]+1,curr[1]])
                            if curr[1] + 1 < len(grid[0]):
                                if grid[curr[0]][curr[1]+1] == 1:
                                    stack.append([curr[0],curr[1]+1])
                        if island_count > max_island_count:
                            max_island_count = island_count
                            #print(max_island_count)
        return max_island_count