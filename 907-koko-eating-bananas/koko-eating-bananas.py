class Solution:
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def brute_force():
            ans = 0
            for rate in range(1,high + 1):
                curr = 0
                for index in range(len(piles)):
                    curr += ceil(piles[index] / rate)
                if curr <= h:
                    return rate
        
        def optimized():
            low = 1
            high = max(piles)
            ans = 0
            while low <= high:
                mid = (low + high) // 2
                curr = 0
                for pile in piles:
                    curr += ceil(pile / mid)
                if curr <= h:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return ans

        return optimized()
