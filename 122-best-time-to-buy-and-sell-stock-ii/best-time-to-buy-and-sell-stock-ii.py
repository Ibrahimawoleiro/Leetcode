class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 0
        profit = 0
        curr = 0
        last = 0
        while(j < len(prices)):
            if i == j:
                j+=1
                continue
            if prices[j] > prices[j - 1]:
                print(prices[j], prices[i])
                if j == len(prices) - 1 and prices[j - 1] - prices[i] < prices[j] - prices[i]:
                    profit += (prices[j] - prices[i])
                    j+=1
                    continue
                j += 1
            else:
                profit += (prices[j - 1] - prices[i])
                i = j
                j += 1
        return profit
            
            