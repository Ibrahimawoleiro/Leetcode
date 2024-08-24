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

    // // TC -> O(N * AMOUNT * 2)
    // // SC -> O(N * AMOUNT + N)
    // int memoized(vector<int>& coins,vector<vector<int>>& dp, int index, int rem){
    //     if(index == 0){
    //         if (rem % coins[index] == 0) return rem / coins[index];
    //         return INT_MAX;
    //     }
    //     if (dp[index][rem] != -1){
    //         return dp[index][rem];
    //     }
    //     int not_take = 0 + memoized(coins,dp, index - 1, rem);
    //     int take = INT_MAX;
    //     if (coins[index] <= rem){
    //         int curr = memoized(coins,dp, index, rem - coins[index]);
    //         if (curr != INT_MAX){
    //             take = 1 + curr;
    //         }
    //     } 
    //     dp[index][rem] = min(not_take, take);
    //     return dp[index][rem];
    // }

    // TC -> O(N * AMOUNT * 2)
    // SC -> O(N * AMOUNT)
    int tabulation(vector<int>& coins,int amount){
         vector<vector<int>> dp(coins.size(), vector<int>(amount + 1, -1));
         int row_size = dp.size();
         for(int index = 0; index < row_size; index++){
            for (int c = 0; c < amount + 1; c++){
                if (index == 0){
                    if (c % coins[0] == 0){
                        dp[index][c] = c / coins[0];
                    }else{
                        dp[index][c] = INT_MAX;
                    }
                }else{
                    int not_take = dp[index - 1][c];
                    int take = INT_MAX;
                    if (coins[index] <= c){
                       int curr = dp[index][c - coins[index]];
                        if (curr != INT_MAX){
                            take = 1 + curr;
                        } 
                    }
                    dp[index][c] = min(not_take, take);
                }
            }
         }
         return dp[row_size - 1][amount];
    }

    int coinChange(vector<int>& coins, int amount) {
       
        int ans = tabulation(coins, amount);
        if (ans != INT_MAX){
            return ans;
        }
        return -1;
    }
};