class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l = 0
        h = len(bloomDay) - 1
        print(min(bloomDay))
        print(max(bloomDay))
        days = bloomDay.copy()
        days.sort()
        
        ans = float('inf')

        #Use a binary search through the days options
        while l <= h:
            #Get the middle day 
            mid = (l + h) // 2
            curr = days[mid]

            i = 0
            j = k - 1

            #Initialize a counter for the number of m length you can get from taking days[mid]
            count = 0
            #Check if you have enough k flowers which are less than or equal days[mid]
            while(j < len(bloomDay)):
                a = i
                while(a <= j):
                    if bloomDay[a] > curr:
                        break
                    a += 1
                if a <= j:
                    i = a + 1
                    j = i + k - 1
                    continue
                if a == j + 1:
                    count += 1
                
                i = j + 1
                j = j + k

            if count >= m:
                if days[mid] < ans:
                    ans = days[mid]
                h = mid - 1
            else:
                l = mid + 1

        return ans if ans < float('inf') else -1


        
