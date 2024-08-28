class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min_left = prices[0];
        int ans = 0;
        for(int i = 0; i < prices.size(); i++){
            ans = max(ans, prices[i] - min_left);
            min_left = min(prices[i], min_left);
        }

        return ans;
    }
};