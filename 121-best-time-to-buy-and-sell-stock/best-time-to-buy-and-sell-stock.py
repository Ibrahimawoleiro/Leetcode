class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # #Approach 1
        # maximum = 0
        # for index in range(len(prices)):
        #     for right_of_index in range(index+1,len(prices)):
        #         if maximum < prices[right_of_index] - prices[index]:
        #             maximum =  prices[right_of_index] - prices[index]
        
        # return maximum

        #Appraoch 2

        maximum = 0
        left = 0
        right = 0

        while(right < len(prices)):
            if left == right:
                right+=1
                continue
            if prices[right] - prices[left] > maximum:
                maximum = prices[right] - prices[left] 
            
            if prices[right] < prices[left]:
                left = right
            
            right +=1
            
        
        return maximum
