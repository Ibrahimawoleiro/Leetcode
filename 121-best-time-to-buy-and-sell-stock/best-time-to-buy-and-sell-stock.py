class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #Approach1
        if len(prices) == 1: 
            return 0

        maximumOverall = 0
        left = 0
        right = 1
        while(right < len(prices)):
            if prices[right] <= prices[left]:
                if(left+1 < right):
                    left+=1
                else:
                    left+=1
                    right+=1
            else:
                if(prices[right] > prices[left]):
                    temp = prices[right] - prices[left]
                    if(temp > maximumOverall):
                        maximumOverall =  temp
                    right+=1

        return maximumOverall

