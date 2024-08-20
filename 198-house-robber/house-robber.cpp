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

    // // TC -> O(N)
    // // SC -> O(N + N)
    // int memoized(vector<int>& nums, vector<int>& dp,  int index){
    //     if (index < 0) return 0;
    //     if (index == 0) return nums[0];
    //     if (dp[index] != -1) return dp[index];
    //     int pick = nums[index] + memoized(nums,dp, index - 2);
    //     int not_pick = memoized(nums,dp, index - 1);
    //     dp[index] = max(pick, not_pick);
    //     return dp[index];
    // }

    //
    int tabulation(vector<int> nums){
        int size = nums.size();
        vector<int> dp(size, -1);
        dp[0] = nums[0];
        for (int i = 1; i<= size - 1; i++){
            int not_pick = dp[i - 1];
            int pick = nums[i];
            if (i - 2 >= 0){
                pick = nums[i] + dp[i - 2];
            }

            dp[i] = max(not_pick, pick);
        }

        return dp[size - 1];
    }

    int rob(vector<int>& nums) {
        return tabulation(nums);
    }
};