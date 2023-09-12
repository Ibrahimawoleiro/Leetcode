class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # Wall is + and empty cell is .
        """
        Create a variable neighbor count = 1
        Get the entrance of the person
        Declare a variable called shortest_path_count
        put the first place in a queue and mark it as passed by putting k into current.
        Queue is going to run as long as there's still something left in the queue
        increase shortest_path_count by 1
            Create a for loop that runs through len(neighbor_count)
                Create variable next_level_count = 0
                Now check for the other places to go from current
                    Put all this options into the queue while increasing next_level_count by 1
        After the for loop, assign the value of next_level_count to neighbor_count
        Once we find a case where val of current is at the edge of the square,returnshortest_path_count
        If we don't find a case where shortest_path_count is at the edge and we are done with bfs, 
        return -1
        """
        count = 0
        neighbor_count = 1
        shortest_path_count = -1
        queue = deque()
        queue.append(entrance)
        print(count)
        while queue:
            count+=1
            print(count)
            print(queue)
            shortest_path_count += 1
            next_level_count = 0
            for option in range(neighbor_count):
                curr = queue.popleft()
                row = curr[0]
                column = curr[1]
                if [row,column] != entrance and (row == len(maze)-1 or row== 0 or column == 0 or column == len(maze[0])-1):
                    return shortest_path_count
                
                maze[curr[0]][curr[1]] = "k"
                
                if curr[0]+1 < len(maze) and maze[curr[0]+1][curr[1]] == ".":
                    queue.append([curr[0]+1,curr[1]])
                    next_level_count+=1
                    maze[curr[0]+1][curr[1]] = "k"
                        
                if curr[0]-1 >= 0 and maze[curr[0]-1][curr[1]] == ".":
                    queue.append([curr[0]-1,curr[1]])
                    next_level_count+=1
                    maze[curr[0]-1][curr[1]] = "k"
                
                if curr[1]+1 < len(maze[0]) and maze[curr[0]][curr[1]+1] == ".":
                    queue.append([curr[0],curr[1]+1])
                    next_level_count+=1
                    maze[curr[0]][curr[1]+1] = "k"
                
                if curr[1]-1 >=0 and maze[curr[0]][curr[1]-1] == ".":
                    queue.append([curr[0],curr[1]-1])
                    next_level_count+=1
                    maze[curr[0]][curr[1]-1] = "k"
                    
            neighbor_count = next_level_count
            
        return -1
                    
        
        