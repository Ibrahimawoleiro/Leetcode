class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        ans = 0

        while low <= high:
            capacity = (low + high) // 2
            days_taken = 0
            total = 0
            for index in range(len(weights)):
                if total + weights[index] <= capacity:
                    total += weights[index]
                    if index == len(weights) - 1:
                        days_taken += 1
                else:
                    days_taken += 1
                    total = weights[index]
                    if index == len(weights) - 1:
                        days_taken += 1

            if days_taken <= days:
                ans = capacity
                high = capacity - 1
            else:
                low = capacity + 1
        return ans
