import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        distance = [[float('inf') for num in range(len(heights[0]))] for number in range(len(heights))]

        heap = []
        #(distance to curr, row, col)
        heapq.heappush(heap, (0, 0, 0))
        
        #distance to each coordinate
        # distance = {}
        completed = set()
        # for row in range(len(heights)):
        #     for col in range(len(heights)):
        #         distance[(row, col)] = float(inf)
        ans = -1
        while heap:
            dist , row, col = heapq.heappop(heap)
            print(dist, row, col)
            if (row, col) in completed or distance[row][col] < dist:
                continue
            
            distance[row][col] = dist
            ans = max(dist, ans)
            completed.add((row, col))
            if (len(heights) - 1, len(heights[0]) - 1) in completed:
                return ans

            if row > 0:
                heapq.heappush(heap,( abs(heights[row][col] - heights[row - 1][col]), row - 1, col))
            if row < len(heights) - 1:
                heapq.heappush(heap,( abs(heights[row][col] - heights[row + 1][col]), row + 1, col))
            if col > 0:
                heapq.heappush(heap,( abs(heights[row][col] - heights[row][col - 1]), row, col - 1))
            if col < len(heights[0]) - 1:
                heapq.heappush(heap,( abs(heights[row][col] - heights[row][col + 1]), row, col + 1))
            # if (row, col) == (len(heights) - 1, len(heights[0]) - 1):
            #     return dist 
            


        return ans