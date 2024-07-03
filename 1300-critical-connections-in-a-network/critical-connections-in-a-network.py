class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        #Visited marker
        visited = [-1 for num in range(n)]

        #log values represent [time curr was visited, neighbor or current least time]
        logs = {}

        #I want to first create the graph
        graph = [[] for num in range(n)]

        for connection in connections:
            start = connection[0]
            end = connection[1]

            graph[start].append(end)
            graph[end].append(start)
        ans = []
        #Now we create a dfs that wil run tarjan's algorithm
        def dfs(curr, t, p):
            if visited[curr] == 1:
                return logs[curr][1]
            
            logs[curr] = [t, t]
            visited[curr] = 1
            for n in graph[curr]:
                if n == p:
                    continue
                neighbor_time = dfs(n, t + 1, curr)
                if t < neighbor_time:
                    #print('curr', curr, 'neighbor', n, 'neighbor_time', neighbor_time)
                    ans.append([curr, n])

                elif t >= neighbor_time:
                    logs[curr][1] = min(logs[curr][1],neighbor_time)
            return logs[curr][1]

        dfs(0, 0, -1)
        return ans