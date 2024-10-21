class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = high
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