class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        low = 1
        high = max(bloomDay)
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            bouquet_count = 0
            i = 0
            while i < len(bloomDay):
                flower_count = 0
                for j in range(k):
                    if i + j >= len(bloomDay) or bloomDay[i + j] > mid:
                        i = i + j + 1
                        break
                    flower_count += 1
                if flower_count == k:
                    i = i + k
                    bouquet_count += 1
            if bouquet_count >= m:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans