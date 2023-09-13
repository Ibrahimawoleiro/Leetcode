class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks) == 1:
            return 0
        heap = []
        heapify(heap)
        for val in sticks:
            heappush(heap,val)
            
        List = []
        ans = 0
        num = 0
        while len(heap) > 1:
            num = heappop(heap)
            num += heappop(heap)
            List.append(num)
            heappush(heap,num)

        for num in List:
            ans+=num
        #ans+=heappop(heap)
        
        return ans
        