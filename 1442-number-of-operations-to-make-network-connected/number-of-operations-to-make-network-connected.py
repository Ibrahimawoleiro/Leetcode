class Union_find:
    
    def __init__(self,V:int):
        self.rank = [0 for _ in range(V)]
        self.ultimate_parent = [val for val in range(V)]
        self.size = [1 for _ in range(V)]
    def find_ultimate_parent(self,vertex):
        ulp_vertex = self.ultimate_parent[vertex]
        curr = vertex
        while ulp_vertex != vertex:
            vertex = ulp_vertex
            ulp_vertex = self.ultimate_parent[ulp_vertex]
            
        self.ultimate_parent[curr] = ulp_vertex
        return ulp_vertex
        
    def find(self,v1:int , v2:int):
        v1_ultimate_parent = self.find_ultimate_parent(v1)
        v2_ultimate_parent = self.find_ultimate_parent(v2)
        return v1_ultimate_parent == v2_ultimate_parent
        
    def union_by_rank(self,v1, v2):
        v1_ultimate_parent = self.find_ultimate_parent(v1)
        v2_ultimate_parent = self.find_ultimate_parent(v2)
        if self.rank[v1_ultimate_parent] > self.rank[v2_ultimate_parent]:
            self.ultimate_parent[v2_ultimate_parent] = v1_ultimate_parent
        elif self.rank[v2_ultimate_parent] > self.rank[v1_ultimate_parent]:
            self.ultimate_parent[v1_ultimate_parent] = v2_ultimate_parent
        else:
            self.rank[v1_ultimate_parent] += 1
            self.ultimate_parent[v2_ultimate_parent] = v1_ultimate_parent
            
    def union_by_size(self,v1, v2):
        v1_ultimate_parent = self.find_ultimate_parent(v1)
        v2_ultimate_parent = self.find_ultimate_parent(v2)
        if self.size[v1_ultimate_parent] > self.size[v2_ultimate_parent]:
            self.ultimate_parent[v2_ultimate_parent] = v1_ultimate_parent
            self.size[v1_ultimate_parent] += self.size[v2_ultimate_parent]
        elif self.rank[v2_ultimate_parent] > self.rank[v1_ultimate_parent]:
            self.ultimate_parent[v1_ultimate_parent] = v2_ultimate_parent
            self.size[v2_ultimate_parent] += self.size[v1_ultimate_parent]
        else:
            self.size[v1_ultimate_parent] += self.size[v2_ultimate_parent]
            self.ultimate_parent[v2_ultimate_parent] = v1_ultimate_parent
    
    def union(self,v1, v2):
        self.union_by_rank(v1, v2)

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
