import queue
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        #Reversed Graph
        adj = [[] for num in range(len(graph))]
        indegrees = [0 for num in range(len(graph))]

        
        
        for c in range(len(graph)):
            for n in graph[c]:
                adj[n].append(c)

        for c in adj:
            for n in c:
                indegrees[n] += 1

        ans = []  
        q = queue.Queue()
        for i in range(len(graph)):
            if indegrees[i] == 0:
                q.put(i)
                
        
        while not q.empty():
            curr = q.get()
            ans.append(curr)
            for n in adj[curr]:
                indegrees[n] -= 1
                if indegrees[n] == 0:
                    q.put(n)
        return sorted(ans)
