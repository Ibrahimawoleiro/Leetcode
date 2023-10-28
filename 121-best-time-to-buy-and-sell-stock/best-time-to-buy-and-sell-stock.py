class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0 or len(prices) ==1:
            return 0
        curr_max = 0

        left = 0
        right = 1

        while(right < len(prices)):
            if (prices[left] < prices[right]) and (prices[right] - prices[left]) > curr_max:
                curr_max = prices[right] - prices[left]
            elif(prices[right] < prices[left]) :
                left = right
            
            right+=1
        
        return curr_max