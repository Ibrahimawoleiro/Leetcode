class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = 1
        h = sum(weights)
        ans = float('inf')
        while l <= h:
            mid = (l + h) // 2
            total = 0
            count = 0
            ReachEnd = True
            for i in range(len(weights)):
                if weights[i] > mid:
                    ReachEnd = False
                    break
                total += weights[i]
                if total >= mid:
                    if total > mid:
                        total = weights[i]
                    else:
                        total = 0
                    count += 1
                if total > 0 and i == len(weights) - 1:
                    count += 1
            if not ReachEnd:
                l = mid + 1
                continue
            if count <= days:
                if mid < ans:
                    ans = mid
                h = mid - 1
            else:
                l = mid + 1

        return ans
