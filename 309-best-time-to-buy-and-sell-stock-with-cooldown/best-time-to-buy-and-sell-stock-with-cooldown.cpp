class Solution {
public:
    // int recursive(vector<int>& prices,int i, bool bought){
    //     if (i >= prices.size()){
    //         return 0;
    //     }
    //     if (i == prices.size() - 1){
    //         if(bought){
    //             return prices[i];
    //         }else{
    //             return 0;
    //         }
    //     }
    //     int buy = 0;
    //     int sell = 0;
    //     if(!bought){
    //         buy = max(-prices[i] + recursive(prices, i + 1, true), recursive(prices, i + 1, false));
    //     }else{
    //         sell = max(prices[i] + recursive(prices, i + 2, false), recursive(prices, i + 1, true));
    //     }
    //     return max(buy, sell);
    // }

    // int memoized(vector<int>& prices,int i, bool bought, vector<vector<int>>& dp){
    //     if (i >= prices.size()){
    //         return 0;
    //     }
    //     if (i == prices.size() - 1){
    //         if(bought){
    //             return prices[i];
    //         }else{
    //             return 0;
    //         }
    //     }
    //     int index = bought ? 1: 0;
    //     if (dp[i][index] != -1){
    //         return dp[i][index];
    //     }
    //     int buy = 0;
    //     int sell = 0;
    //     if(!bought){
    //         buy = max(-prices[i] + memoized(prices, i + 1, true, dp), memoized(prices, i + 1, false, dp));
    //     }else{
    //         sell = max(prices[i] + memoized(prices, i + 2, false, dp), memoized(prices, i + 1, true, dp));
    //     }
    //     dp[i][index] =  max(buy, sell);
    //     return dp[i][index];
    // }

    int tabulation(vector<int>& prices){
        vector<vector<int>> dp(prices.size(), vector<int>(2, -1));
        int bought = 1;
        int not_bought = 0;
        int last_index = prices.size() - 1;
        dp[last_index][bought] = prices[last_index];
        dp[last_index][not_bought] = 0;

        for(int i = last_index - 1; i >= 0 ; i --){
            dp[i][not_bought] = max(-prices[i]+dp[i + 1][bought], dp[i + 1][not_bought]);
            dp[i][bought] = max(prices[i] + (i + 2 < prices.size() ? dp[i + 2][not_bought]: 0), dp[i + 1][bought]);
        }
        return dp[0][not_bought];
    }

    int maxProfit(vector<int>& prices) {
        return tabulation(prices);
    }
};