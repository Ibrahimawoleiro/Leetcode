class Solution {
public:

    // // TC -> O(N * AMOUNT * 2^N)
    // // SC -> O(N)
    // int recursive(vector<int>& coins, int index, int rem){
    //     if(index == 0){
    //         if (rem % coins[index] == 0) return rem / coins[index];
    //         return INT_MAX;
    //     }
    //     int not_take = 0 + recursive(coins,index - 1, rem);
    //     int take = INT_MAX;
    //     if (coins[index] <= rem){
    //         int curr = recursive(coins, index, rem - coins[index]);
    //         if (curr != INT_MAX){
    //             take = 1 + curr;
    //         }
    //     } 
    //     return min(not_take, take);
    // }

    int memoized(vector<int>& coins,vector<vector<int>>& dp, int index, int rem){
        if(index == 0){
            if (rem % coins[index] == 0) return rem / coins[index];
            return INT_MAX;
        }
        if (dp[index][rem] != -1){
            return dp[index][rem];
        }
        int not_take = 0 + memoized(coins,dp, index - 1, rem);
        int take = INT_MAX;
        if (coins[index] <= rem){
            int curr = memoized(coins,dp, index, rem - coins[index]);
            if (curr != INT_MAX){
                take = 1 + curr;
            }
        } 
        dp[index][rem] = min(not_take, take);
        return dp[index][rem];
    }

    int coinChange(vector<int>& coins, int amount) {

        vector<vector<int>> dp(coins.size(), vector<int>(amount + 1, -1));
        int ans = memoized(coins,dp, coins.size() - 1, amount);
        if (ans != INT_MAX){
            return ans;
        }
        return -1;
    }
};