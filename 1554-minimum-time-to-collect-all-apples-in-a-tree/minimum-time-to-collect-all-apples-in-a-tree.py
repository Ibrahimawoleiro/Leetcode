class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        time = 0
        m = [0]
        graph = [[] for num in range(n)]
        valid_time = [(0,False) for num in range(n)]
        visited = [0 for num in range(n)]
        for edge in edges:
            start = edge[0]
            destination = edge[1]
            graph[start].append(destination)
            graph[destination].append(start)


        def dfs(curr, time):
            
            if visited[curr] == 1:
                return [0, False]
            if hasApple[curr]:
                valid_time[curr] = (time, True)
            visited[curr] = 1
            for neighbor in graph[curr]:
                neighbor_data = dfs(neighbor, time + 1)

                #We need to ask if the path resulted in an apple being found
                if neighbor_data[1]:
                    valid_time[curr] = (neighbor_data[0], True)
                    time = valid_time[curr][0]
            
            valid_time[curr] = (time + 1, valid_time[curr][0])

            return valid_time[curr]
        
        print(valid_time)
        dfs(0,time)[0]
        return valid_time[0][0] - 1

