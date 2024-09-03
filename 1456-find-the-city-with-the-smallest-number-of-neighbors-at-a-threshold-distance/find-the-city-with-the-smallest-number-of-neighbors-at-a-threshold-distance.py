class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        distance = [[100000000 for _ in range(n)] for _ in range(n)]
        for edge in edges:
            s, e, w = edge
            distance[s][e] = w
            distance[e][s] = w 

        for i in range(n):
            distance[i][i] = 0

        for midpoint in range(n):
            for start in range(n):
                for end in range(n):
                    if distance[start][midpoint] + distance[midpoint][end] < distance[start][end]:
                        distance[start][end] = distance[start][midpoint] + distance[midpoint][end]
        
        ans = 100000000
        city = -1
        for r in range(n):
            vertex_connection_count = 0
            for c in range(n):
                if r != c and distance[r][c] <= distanceThreshold:
                    vertex_connection_count+=1
            if vertex_connection_count <= ans:
                ans = vertex_connection_count
                city = r        


        return city                