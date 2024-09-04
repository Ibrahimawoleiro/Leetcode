class Union_find:
    
    def __init__(self,V:int):
        self.rank = [0 for _ in range(V)]
        self.ultimate_parent = [val for val in range(V)]
        self.size = [1 for _ in range(V)]
    def find_ultimate_parent(self,vertex):
        ulp_vertex = self.ultimate_parent[vertex]
        parent = ulp_vertex
        curr = vertex
        while ulp_vertex != vertex:
            vertex = ulp_vertex
            ulp_vertex = self.ultimate_parent[ulp_vertex]
        self.ultimate_parent[curr] = ulp_vertex
        self.ultimate_parent[parent] = ulp_vertex
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
        elif self.size[v2_ultimate_parent] > self.size[v1_ultimate_parent]:
            self.ultimate_parent[v1_ultimate_parent] = v2_ultimate_parent
            self.size[v2_ultimate_parent] += self.size[v1_ultimate_parent]
        else:
            self.size[v1_ultimate_parent] += self.size[v2_ultimate_parent]
            self.ultimate_parent[v2_ultimate_parent] = v1_ultimate_parent
    
    def union(self,v1, v2):
        self.union_by_size(v1, v2)

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        row_size = 0
        col_size = 0
        store = set()
        for location in stones:
            row_size = max(row_size,location[0])
            col_size = max(col_size, location[1])
        row_size += 1
        col_size += 1
        num_of_nodes = row_size + col_size
        u_f = Union_find(num_of_nodes)
        for location in stones:
            x = location[0]
            y = location[1] + row_size 
            u_f.union(x,y)
            store.add(x)
            store.add(y)

        count = 0
        for num in store:
            if num == u_f.find_ultimate_parent(num):
                count += 1
        print(store)
        return len(stones) - count


