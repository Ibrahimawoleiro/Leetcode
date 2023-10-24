class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        island_count = 0
 
        Queue = deque()
        k=0
        for array_index in range(len(grid)):
            for number_index in range(len(grid[array_index])):
                if grid[array_index][number_index] == "1":
                
                    island_count +=1
                    grid[array_index][number_index] = "5"
                    if array_index-1>=0 and grid[array_index-1][number_index]=="1":
                        Queue.append([array_index-1,number_index])
                    if array_index+1<len(grid) and grid[array_index+1][number_index]=="1":
                        Queue.append([array_index+1,number_index])
                    if number_index -1 >= 0 and grid[array_index][number_index-1]=="1":
                        Queue.append([array_index,number_index-1])
                    if number_index + 1 < len(grid[0]) and grid[array_index][number_index+1]=="1":
                        Queue.append([array_index,number_index+1])
             
                    while Queue:
                   
                        curr = Queue.popleft()
                     
                        grid[curr[0]][curr[1]]="5"
                        if curr[0] - 1 >= 0 and grid[curr[0]-1][curr[1]]=="1":
                            Queue.append([curr[0]-1,curr[1]])
                            grid[curr[0]-1][curr[1]]="5"
                
                        if curr[0] + 1 < len(grid) and grid[curr[0]+1][curr[1]] == "1":
                            Queue.append([curr[0]+1,curr[1]])
                            grid[curr[0]+1][curr[1]]="5"
                            
                       
                        if curr[1]-1 >= 0 and grid[curr[0]][curr[1]-1] == "1":
                            Queue.append([curr[0],curr[1]-1])
                            grid[curr[0]][curr[1]-1]="5"
                            
                        if curr[1] + 1 < len(grid[0]) and grid[curr[0]][curr[1]+1] == "1":
                            Queue.append([curr[0],curr[1]+1])
                            grid[curr[0]][curr[1]+1]="5"
                            
                        
        return island_count
                        
                
                        