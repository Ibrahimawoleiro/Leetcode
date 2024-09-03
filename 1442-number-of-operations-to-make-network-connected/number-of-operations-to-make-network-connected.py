

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        

        con_comp_count = 0

        graph = [[] for num in range(n)]
        visited = [0 for num in range(n)]
        def dfs(curr):
            if visited[curr] == 1:
                return 
            visited[curr] = 1
            
            for neighbor in graph[curr]:
                if visited[neighbor ]== 0:
                    dfs(neighbor)

        for connection in connections:
            start , end = connection
            graph[start].append(end)
            graph[end].append(start) 
        
        for num in range(n):
            if visited[num] != 1:
                con_comp_count += 1
                dfs(num)
        if len(connections) < n - 1:
            return -1

        return con_comp_count - 1
