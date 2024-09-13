class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            days_taken = 1
            curr_sum = 0
            for weight in weights:
                if curr_sum + weight <= mid:
                    curr_sum += weight
                else:
                    days_taken += 1
                    curr_sum = weight
            if days_taken <= days:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans