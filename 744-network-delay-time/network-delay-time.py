import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        heap = []
        distance = [float('inf') for num in range(n+1)]
        graph = [[] for num in range(n+1)]
        for connection in times:
            start, end, cost = connection
            graph[start].append([end, cost])
        
        #(curr, sum of cost to current)
        heapq.heappush(heap, (0, k))
        completed = set()
        while heap:
            cost, curr = heapq.heappop(heap)
            if curr in completed or distance[curr] < cost:
                continue

            distance[curr] = cost
            completed.add(curr)

            for n in graph[curr]:
                heapq.heappush(heap, (cost + n[1], n[0]))
        ans = max(distance[1:])
        
        return ans if ans < float('inf') else -1

