import queue
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        q = queue.Queue()
        graph = [[] for num in range(n)]
        for connection in flights:
            start, end, time = connection
            graph[start].append([end, time])

        # print(graph)
        dist = [float('inf') for num in range(n)]
        #(stops, current, cost)
        q.put((0, src, 0))

        while not q.empty():
            stops, curr, cost = q.get()
           
            if cost > dist[curr] or (stops > k and curr != dst):
                continue
            
            dist[curr] = cost

            for n in graph[curr]:
                q.put((stops + 1, n[0], cost + n[1]))

        return dist[dst] if dist[dst] < float('inf') else -1