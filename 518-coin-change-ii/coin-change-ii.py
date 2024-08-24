class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # #TC -> O(N * AMOUNT * 2 ^ N)
        # #SC -> O(N)
        # def recursive(index, rem):
        #     if rem == 0:
        #         return 1
        #     if index == 0:
        #         if rem % coins[index] == 0:
        #             return 1
        #         return 0
        #     not_take = recursive(index - 1, rem)
        #     take = 0
        #     if rem >= coins[index]:
        #         take = recursive(index, rem - coins[index])
        #     return take + not_take

        dp = [[-1 for val in range(amount + 1)] for num in range(len(coins))]

        # def memoized(index, rem, dp):
        #     if rem == 0:
        #         return 1
        #     if index == 0:
        #         if rem % coins[index] == 0:
        #             return 1
        #         return 0
        #     if (dp[index][rem] != -1):
        #         return dp[index][rem]
        #     not_take = memoized(index - 1, rem, dp)
        #     take = 0
        #     if rem >= coins[index]:
        #         take = memoized(index, rem - coins[index], dp)
        #     dp[index][rem] = take + not_take
        #     return dp[index][rem]

        def tabulation():
            dp = [[-1 for _ in range(amount + 1)] for num in range(len(coins))]
            for index in range(len(coins)):
                for goal in range(amount + 1):
                    if index == 0:
                        if goal % coins[index] == 0:
                            dp[index][goal] = 1
                        else:
                            dp[index][goal] = 0
                    else:
                        not_take = dp[index - 1][goal]
                        take = 0
                        if goal >= coins[index]:
                            take = dp[index][goal - coins[index]]
                        dp[index][goal] = take + not_take
            print(dp)
            return dp[len(dp) - 1][amount]
        return tabulation()

