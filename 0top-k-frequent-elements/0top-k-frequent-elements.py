class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dictionary = {}
        
        for val in nums:
            if val not in dictionary:
                dictionary[val] = 1
            else:
                dictionary[val]+=1
                
        heap = []      
        heapq.heapify(heap)
        
        for key, val in dictionary.items():
                heapq.heappush(heap,[val,key])
                if len(heap) > k:
                    print(heapq.heappop(heap))
                
        ans = []
        while(len(heap)>0):
            ans.append(heapq.heappop(heap)[1])
            
        return ans