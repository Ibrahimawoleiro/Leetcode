class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        most_wealth = -1
        for arr in accounts:
            curr = sum(arr)
            if curr > most_wealth:
                most_wealth = curr
        
        return most_wealth