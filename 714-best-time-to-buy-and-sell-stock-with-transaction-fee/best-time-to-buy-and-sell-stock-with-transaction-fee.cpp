class Solution {
public:
    // int recursive(vector<int>& prices,int i, bool bought, int fee){
    //     if (i == prices.size() - 1){
    //         if(bought){
    //             return prices[i] - fee;
    //         }else{
    //             return 0;
    //         }
    //     }
    //     int buy = 0;
    //     int sell = 0;
    //     if(!bought){
    //         buy = max(-prices[i] + recursive(prices, i + 1, true, fee), recursive(prices, i + 1, false, fee));
    //     }else{
    //         sell = max((prices[i] - fee) + recursive(prices, i + 1, false, fee), recursive(prices, i + 1, true, fee));
    //     }
    //     return max(buy, sell);
    // }

    int memoized(vector<int>& prices,int i, bool bought, vector<vector<int>>& dp, int fee){
        if (i == prices.size() - 1){
            if(bought){
                return prices[i] - fee;
            }else{
                return 0;
            }
        }
        int index = bought ? 1: 0;
        if (dp[i][index] != -1){
            return dp[i][index];
        }
        int buy = 0;
        int sell = 0;
        if(!bought){
            buy = max(-prices[i] + memoized(prices, i + 1, true, dp, fee), memoized(prices, i + 1, false, dp, fee));
        }else{
            sell = max((prices[i]-fee) + memoized(prices, i + 1, false, dp, fee), memoized(prices, i + 1, true, dp, fee));
        }
        dp[i][index] =  max(buy, sell);
        return dp[i][index];
    }

    int maxProfit(vector<int>& prices, int fee) {
        vector<vector<int>> dp(prices.size(), vector<int>(2, -1));
        return memoized(prices, 0, false, dp, fee);
    }
};