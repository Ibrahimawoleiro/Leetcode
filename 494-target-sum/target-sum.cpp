class Solution {
public:
    // // TC -> O(N * TARGET * 2 ^ N)
    // // SC -> O(N)
    // int recursive(vector<int>& nums, int target,int sum, int index){
    //     cout << target <<' '<< sum << endl;
    //     if (index == 0){
    //         int ans = 0;
    //         if((target == sum + nums[0])){
    //             ans ++;
    //         } 
    //         if ((target == sum - nums[0])){
    //             ans++;
    //         }
    //         return ans;
    //     }
    //     int negative = recursive(nums, target,sum + (-nums[index]), index - 1);
    //     int positive = recursive(nums, target,sum + (nums[index]), index - 1);
    //     return negative + positive;
    // }

    int memoized(vector<int>& nums,vector<vector<int>>& dp ,int target,int sum, int index,int offset){
        if (index == 0){
            int ans = 0;
            if(target == (sum + nums[0])){
                ans ++;
            } 
            if (target == (sum - nums[0])){
                ans++;
            }
            return ans;
        }
        if (dp[index][sum + offset] != 100000000){
            return dp[index][sum + offset];
        }
        int negative = memoized(nums, dp, target,sum + (-nums[index]), index - 1, offset);
        int positive = memoized(nums, dp, target,sum + (nums[index]), index - 1, offset);
        dp[index][sum + offset] = negative + positive;
        return dp[index][sum + offset];
    }

    int findTargetSumWays(vector<int>& nums, int target) {
        int offset = 0;
        for (int num: nums){
            offset += num;
        }
        vector<vector<int>> dp(nums.size(), vector<int>(2 * offset + 1, 100000000));
        return memoized(nums, dp, target, 0, nums.size() - 1, offset);
    }
};