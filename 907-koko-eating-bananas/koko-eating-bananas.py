class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = sum(piles)
        ans = 10 ** 10
        while low <= high:
            mid = (low + high) // 2
            time = 0
            for pile in piles:
                time += ceil(pile/mid)
            if time <= h:
                ans = min(ans, mid)
                high = mid - 1
            else:
                low = mid + 1
        return ans