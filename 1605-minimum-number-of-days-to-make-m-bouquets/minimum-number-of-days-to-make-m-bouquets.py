class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        low = 1

        high = max(bloomDay)

        ans = -1

        while low <= high:

            mid = (low + high) // 2

            bouquets = 0

            adj_count = 0

            for val in bloomDay:

                if val <= mid:

                    adj_count += 1

                else:

                    adj_count = 0

                if adj_count == k:

                    bouquets += 1

                    adj_count = 0

            if bouquets >= m:

                ans = mid

                high = mid - 1
            
            else:

                low = mid + 1

        
        return ans
                