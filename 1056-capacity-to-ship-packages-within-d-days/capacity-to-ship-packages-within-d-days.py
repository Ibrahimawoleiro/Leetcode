class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        left =  max(weights)

        right = sum(weights)

        ans = right

        while left <= right:

            mid = (left + right) // 2

            total = 0

            count = 0

            for val in weights:

                if total + val <= mid:

                    total += val

                else:

                    count += 1

                    total = val

            if total > 0:
                count += 1

            if count <= days:

                ans = mid 

                right = mid - 1
            
            else:

                left = mid + 1

        return ans

