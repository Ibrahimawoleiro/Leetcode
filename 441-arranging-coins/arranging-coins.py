class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 1
        h = n
        ans = 0
        while l <= h:
            mid = (l + h) // 2
            total = (mid / 2) * (mid + 1)
            if total == n:
                return mid

            elif total < n:
                l = mid + 1
                ans = mid
            else:
                h = mid - 1
        return ans