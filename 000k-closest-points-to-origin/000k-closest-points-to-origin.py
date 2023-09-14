class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        √(x1 - x2)2 + (y1 - y2)2)
        """
        heap = []
        heapify(heap)
        curr_distance = 0
        for List in points:
            curr_distance = math.sqrt(List[0]**2 + List[1]**2)
            print(curr_distance, List)
            heappush(heap,[-curr_distance,List])
            if(len(heap)>k):
                print(heappop(heap))
            
        ans = []
          
        for num in range(len(heap)):
            ans.append(heappop(heap)[1])
        
        return ans