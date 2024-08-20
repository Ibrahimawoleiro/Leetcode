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

    // TC -> O(N)
    // SC -> O(N + N)
    int memoized(vector<int>& nums,vector<int>& dp, int index){
        if (index < 0) return 0;
        if (index == 0) return nums[0];
        if (dp[index] != -1) return dp[index];

        int not_take = memoized(nums, dp, index - 1);

        int take = nums[index] +  memoized(nums, dp, index - 2);

        dp[index] = max(not_take, take);

        return dp[index];
    }

    int rob(vector<int>& nums) {
        if (nums.size() == 1){
            return nums[0];
        }
        vector<int> omit_f(nums.begin()+1, nums.end());
        vector<int> omit_l(nums.begin(), nums.begin() + nums.size() - 1);
        vector<int> dp_f(nums.size(), -1);
        vector<int> dp_l(nums.size(), -1);
        return max(memoized(omit_f, dp_f, omit_f.size() - 1), memoized(omit_l, dp_l,  omit_l.size() - 1));
    }
};