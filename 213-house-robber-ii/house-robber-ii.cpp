class Solution {
public:
    // // TC -> O(2 ^ N)
    // // SC -> O(1)
    // int recursive(vector<int>& nums, int index){
    //     if (index < 0){
    //         return 0;
    //     }
    //     if (index == 0){
    //         return nums[0];
    //     }

    //     int not_take = recursive(nums, index - 1);
    //     int take = nums[index] + recursive(nums,index - 2);

    //     return max(not_take, take);
    // }

    // // TC -> O(N)
    // // SC -> O(N + N)
    // int memoized(vector<int>& nums,vector<int>& dp, int index){
    //     if (index < 0) return 0;
    //     if (index == 0) return nums[0];
    //     if (dp[index] != -1) return dp[index];

    //     int not_take = memoized(nums, dp, index - 1);

    //     int take = nums[index] +  memoized(nums, dp, index - 2);

    //     dp[index] = max(not_take, take);

    //     return dp[index];
    // }

    int tabulation(vector<int>& nums){
        vector<int> dp(nums.size(), -1);
        dp[0] = nums[0];

        for(int i = 1; i < nums.size(); i++){

            int not_take = dp[i - 1];
            int take = nums[i];
            if (i - 2 >= 0){
                take = nums[i] + dp[i - 2];
            }

            dp[i] = max(take, not_take);
        }

        return dp[nums.size() - 1];
    }
    int rob(vector<int>& nums) {
        if (nums.size() == 1){
            return nums[0];
        }
        vector<int> omit_f(nums.begin()+1, nums.end());
        vector<int> omit_l(nums.begin(), nums.begin() + nums.size() - 1);
        return max(tabulation(omit_f), tabulation(omit_l));
    }
};