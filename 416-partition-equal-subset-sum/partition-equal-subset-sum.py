class Solution:
    def recursive(self,arr, rem, index):
        if rem < 0 or index < 0: 
            return False
        if rem == 0:
            return True
        take = self.recursive(arr, rem - arr[index], index - 1)
        not_take = self.recursive(arr, rem, index - 1)
        return take or not_take
    
    def memoized(self,arr, rem, index, dp):
        if rem == 0:
            return True
        if rem < 0 or index < 0: 
            return False
        if dp[index][rem] != -1:
            return dp[index][rem]
        take = self.memoized(arr, rem - arr[index], index - 1, dp)
        not_take = self.memoized(arr, rem, index - 1, dp)
        dp[index][rem] = take or not_take
        return dp[index][rem]
    
    def tabulation(self,arr, N, sum):
        dp = [[False for _ in range(sum + 1)] for _ in range(N)]
        for index in range(N):
            dp[index][0] = True
        for index in range(N):
            for rem in range(sum + 1):
                if rem == 0:
                    dp[index][rem] = True
                else:
                    take = False
                    not_take = False
                    if rem - arr[index] >= 0:
                        take = dp[index - 1][rem - arr[index]]
                    not_take = dp[index - 1][rem]
                    dp[index][rem] = take or not_take
        return dp[N - 1][sum]
    
    def optimized_tabulation(self, arr, N, sum):
        prev = [False for _ in range(sum + 1)] 
        curr = [False for _ in range(sum + 1)] 
        for index in range(N):
            for rem in range(sum + 1):
                if rem == 0:
                    curr[rem] = True
                else:
                    take = False
                    if rem - arr[index] >= 0:
                        remainder = rem - arr[index]
                        if remainder == 0 and index == 0:
                            take = True
                        else:
                            take = prev[rem - arr[index]]
                    not_take = prev[rem]
                    curr[rem] = take or not_take
            prev, curr = curr, prev
        return prev[sum]

    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        return self.optimized_tabulation(nums, n - 1, target)