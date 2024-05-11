class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dic = {}

        def helper(rem):
            if rem == 0:
                return 0
            elif rem < 0:
                return -1
            
            if rem in dic:
                return dic[rem]

            minimum = -1

            for coin in coins:
                remainder = rem - coin
                res = helper(remainder)
                if res >= 0:
                    if minimum > 0:
                        minimum = min(minimum, res + 1)
                    else:
                        minimum = res + 1
                    
            dic[rem] = minimum
            return minimum

        return helper(amount)
