class Solution {
public:
    // // TC -> O(2 ^ N)
    // // SC -> O(1)
    // int recursive(vector<int>& nums, int index){
    //     if (index < 0 ){
    //         return 0;
    //     }
    //     if (index  == 0) return nums[0];

    //     int pick = nums[index] + recursive(nums, index - 2);

    //     int not_pick = recursive(nums,index - 1);

    //     return max(pick, not_pick);
    // }

    int memoized(vector<int>& nums, vector<int>& dp,  int index){
        if (index < 0) return 0;
        if (index == 0) return nums[0];
        if (dp[index] != -1) return dp[index];
        int pick = nums[index] + memoized(nums,dp, index - 2);
        int not_pick = memoized(nums,dp, index - 1);
        dp[index] = max(pick, not_pick);
        return dp[index];
    }

    int rob(vector<int>& nums) {
        vector<int> dp(nums.size(), -1);
        return memoized(nums,dp, nums.size() - 1);
    }
};