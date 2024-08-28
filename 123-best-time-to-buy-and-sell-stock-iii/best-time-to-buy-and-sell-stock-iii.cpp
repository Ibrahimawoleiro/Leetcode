class Solution {
public:
    // int recursive(vector<int>& prices,int index, int rem, bool bought){
    //     if (rem <= 0){
    //         return 0;
    //     }
    //     if (index == prices.size() - 1){
    //         if (bought){
    //             return prices[index];
    //         }else{
    //             return 0;
    //         }
    //     }
    //     int buy = 0;
    //     int sell = 0;
    //     if(!bought){
    //         buy = max(-prices[index] + recursive(prices, index + 1, rem, true), recursive(prices, index + 1, rem, false));
    //     }else{
    //         sell = max(prices[index] + recursive(prices, index + 1, rem - 1, false), recursive(prices, index + 1, rem, true));
    //     }
    //     return max(buy, sell);
    // }

    // int memoized(vector<int>& prices,int index, int rem, bool bought, vector<vector<vector<int>>>& dp){
    //     if (rem <= 0){
    //         return 0;
    //     }
    //     if (index == prices.size() - 1){
    //         if (bought){
    //             return prices[index];
    //         }else{
    //             return 0;
    //         }
    //     }
    //     int transaction = bought ? 1: 0;
    //     // cout << index << " " << rem << " "<< transaction << endl;
    //     if (dp[index][rem][transaction] != -1){
    //         return dp[index][rem][transaction];
    //     }
    //     int buy = 0;
    //     int sell = 0;
    //     if(!bought){
    //         buy = max(-prices[index] + memoized(prices, index + 1, rem, true, dp), memoized(prices, index + 1, rem, false, dp));
    //     }else{
    //         sell = max(prices[index] + memoized(prices, index + 1, rem - 1, false, dp), memoized(prices, index + 1, rem, true, dp));
    //     }
    //     dp[index][rem][transaction] = max(buy, sell);
    //     return dp[index][rem][transaction];
    // }

    int tabulation(vector<int>& prices){
        vector<vector<vector<int>>> dp(prices.size(), vector<vector<int>>(3, vector<int>(2, 0)));
        for(int index = prices.size() - 1; index >= 0; index--){
            for(int bought = 0; bought <= 1; bought++){
                for(int rem = 0; rem <= 2; rem ++){
                    if (rem == 0){
                        dp[index][rem][bought] = 0;
                    }else if(index == prices.size() - 1){
                        if (bought == 1){
                            dp[index][rem][bought] = prices[index];
                        }
                    }else{
                        int buy = 0;
                        int sell = 0;
                        if(bought == 0){
                            buy = max(-prices[index] + dp[index + 1][rem][1], dp[index + 1][rem][0]);
                        }else{
                            sell = max(prices[index] + dp[index + 1][rem - 1][0],dp[index + 1][rem][1]);
                        }
                        dp[index][rem][bought] = max(buy, sell);
                    }
                }
            }
        }
        return dp[0][2][0];
    }

    int maxProfit(vector<int>& prices) {
        
        return tabulation(prices);
    }
};