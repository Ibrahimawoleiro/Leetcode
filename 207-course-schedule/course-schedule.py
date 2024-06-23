class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        
        
        adj = [[] for num in range(numCourses)]

        visited = [0 for num in range(numCourses)]

        curr_path = [0 for num in range(numCourses)]
        
        for r in prerequisites:
            adj[r[1]].append(r[0])

        def dfs(curr):
            if curr_path[curr] == 1:
                return False
            
            if visited[curr] == 1:
                return True
            visited[curr] = 1
            curr_path[curr] = 1

            for n in adj[curr]:
                if not dfs(n):
                    return False

            curr_path[curr] = 0
            return True
        
        for n in range(numCourses):
            if visited[n] == 0:
                if not dfs(n):
                    return False

        
        return True
