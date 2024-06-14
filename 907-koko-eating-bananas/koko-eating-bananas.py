class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        u = max(piles)
        ans = float('inf')
        while l <= u:
            mid = (l + u) // 2
            total = 0
            for num in piles:
                total += ceil(num / mid)
            if total <= h:
                if mid < ans:
                    ans = mid
                u = mid - 1
            else:
                l = mid + 1

        return ans