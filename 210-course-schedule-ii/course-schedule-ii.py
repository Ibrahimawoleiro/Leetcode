import queue
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for num in range(numCourses)]

        visited = [0 for num in range(numCourses)]

        curr_path = [0 for num in range(numCourses)]
        def NoCycle():
            
            
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
        
        if NoCycle():
            def topoSort(V, adj):
                # Code here
                indegree = [0 for num in range(V)]
                ans = []
                q = queue.Queue()
                for connection in adj:
                    for n in connection:
                        indegree[n] +=1
                        
                for i in range(V):
                    if indegree[i] == 0:
                        q.put(i)
                        
                
                while not q.empty():
                    curr = q.get()
                    ans.append(curr)
                    for n in adj[curr]:
                        indegree[n] -= 1
                        if indegree[n] == 0:
                            q.put(n)
                
                
                
                return ans
            return topoSort(numCourses, adj)
            
        return []