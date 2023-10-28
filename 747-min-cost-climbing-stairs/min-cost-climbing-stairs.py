class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        dictionary={
           len(cost)-1 : cost[len(cost)-1]
        }
       
        return min(self.helper(dictionary,cost,0),dictionary[1])
        
    def helper(self,dictionary,arr,current):
        if current == len(arr):
            return 0
        
        if current == len(arr) -1:
            return arr[current]
        if current in dictionary:
            return dictionary[current]
        min_cost = 0
        one_jump = arr[current]+ self.helper(dictionary,arr,current+1)
        two_jumps = arr[current] + self.helper(dictionary,arr,current+2)
        min_cost += min(one_jump,two_jumps)
        dictionary[current]=min_cost
        
        return min_cost