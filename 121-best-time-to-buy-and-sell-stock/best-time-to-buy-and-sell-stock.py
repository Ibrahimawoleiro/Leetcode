class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        curr_max = 0

        left = 0
        right = 1

        while(right < len(prices)):
            if (prices[left] < prices[right]):
                if  (prices[right] - prices[left]) > curr_max:
                    curr_max = prices[right] - prices[left]
            else:
                left = right
            
            right+=1
        
        return curr_max