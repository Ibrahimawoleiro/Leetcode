class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) == 1:
            return 0

        j = 1
        diff = [0]
        while j < len(prices):
            diff.append(prices[j] - prices[j - 1])
            j += 1

        m = diff[0]
        curr = diff[0]
        for index in range(1, len(diff)):
            if curr + diff[index] > diff[index]:
                curr += diff[index]
                if curr > m:
                    m = curr
            else:
                curr = diff[index]
                if curr > m:
                    m = curr

        return m
                
