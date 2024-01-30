class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = {}

        def helper(curr):
            if curr < 0:
                return curr
            
            if curr == 0:
                return 0
            
            if curr in dp:
                return dp[curr]

            smallest = 2 ** 33

            for val in coins:
                path = helper(curr - val)
                if path >=0 and  path < smallest:
                    smallest = path
            if smallest == 2 ** 33:
                dp[curr] = -1
                return -1
            dp[curr] = 1 + smallest
            return dp[curr]

        return helper(amount)