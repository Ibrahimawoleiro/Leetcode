class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        def brute_force():
            low = 1
            high = max(bloomDay)
            for days in (range(1, high + 1)):
                bouquet = 0
                flowers = 0
                for flower_index in range(len(bloomDay)):
                    if bloomDay[flower_index] <= days:
                        flowers += 1
                        if flowers == k:
                            bouquet += 1
                            flowers = 0
                    else:
                        flowers = 0
                if bouquet == m:
                    return days
            return -1
        def optimized():
            low = 1
            high = max(bloomDay)
            ans = -1
            while low <= high:
                mid = (low + high) // 2
                bouquet = 0
                flowers = 0
                for flower_bloom in bloomDay:
                    if  flower_bloom <= mid:
                        flowers += 1
                        if flowers == k:
                            bouquet += 1
                            flowers = 0
                    else:
                        flowers = 0
                if bouquet >= m:
                    ans = mid
                    high = mid - 1
                elif bouquet < m:
                    low = mid + 1
                else:
                    high =  mid - 1 
            return ans
        return optimized()
