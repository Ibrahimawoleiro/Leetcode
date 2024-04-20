import heapq
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        min_heap = []
        for val in nums:
            heapq.heappush(min_heap,val)
        while(k>0):
            curr = heapq.heappop(min_heap)
            curr *= -1
            heapq.heappush(min_heap,curr)
            k-=1
        return sum(min_heap)