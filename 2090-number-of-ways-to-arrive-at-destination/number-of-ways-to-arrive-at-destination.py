import heapq
from typing import List

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7

        distance = [float('inf')] * n
        ways = [0] * n
        graph = [[] for _ in range(n)]
        
        for start, end, cost in roads:
            graph[start].append((end, cost))
            graph[end].append((start, cost))
        
        heap = [(0, 0)]  # (cost, node)
        distance[0] = 0
        ways[0] = 1
        
        while heap:
            curr_cost, curr = heapq.heappop(heap)
            
            if curr_cost > distance[curr]:
                continue
            
            for neighbor, weight in graph[curr]:
                new_cost = curr_cost + weight
                
                if new_cost < distance[neighbor]:
                    distance[neighbor] = new_cost
                    ways[neighbor] = ways[curr]
                    heapq.heappush(heap, (new_cost, neighbor))
                elif new_cost == distance[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[curr]) % MOD
        
        return ways[n - 1] % MOD
