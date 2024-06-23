class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        color = [-1 for num in range(len(graph))]

        def dfs(n, c):
            if color[n] > -1:
                return
            color[n] = c

            valid = True
            for neighbor in graph[n]:
                #Go down the path 
                if color[neighbor] < 0:
                    valid =  dfs(neighbor, 0 if c == 1 else 1)
                    if valid == False:
                        return False
                #ignore or return False
                else:
                    if c == 0 and color[neighbor] == 0 or c == 1 and color[neighbor] == 1:
                        return False
            return valid

        for n in range(len(graph)):
            if color[n] == -1:
                if not dfs(n, 0):
                    return False
        return True