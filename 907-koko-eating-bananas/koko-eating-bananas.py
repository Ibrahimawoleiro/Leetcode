class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        low = 1

        high = max(piles)

        ans = 0

        total = float('inf')

        while low <= high:

            mid = (low + high) // 2

            curr_total = 0

            for val in piles:

                curr_total += math.ceil((val / mid))

            if curr_total <= h:

                ans = mid

                total = curr_total

                high = mid - 1
            
            else: 

                low = mid + 1

        return ans 

