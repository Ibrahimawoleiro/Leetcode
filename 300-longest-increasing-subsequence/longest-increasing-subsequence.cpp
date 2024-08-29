class Solution {
public:
    // int recursive(vector<int>& nums, int index, int last){
    //     if (index == 0){
    //         if (last > nums[index]) return 1;
    //         return 0;
    //     }

    //     int not_take = recursive(nums, index - 1, last);
    //     int take = 0;
    //     if (last > nums[index]){
    //         take = 1 + recursive(nums, index - 1, nums[index]);
    //     }
    //     return max(not_take, take);
    // }

    int memoized(vector<int>& nums, int index, int last, vector<vector<int>>& dp, int maximum){
        if (index == 0){
            if (last > nums[index]) return 1;
            return 0;
        }
        if(dp[index][last+maximum] != -1){
            return dp[index][last+maximum];
        }
        int not_take = memoized(nums, index - 1, last, dp, maximum);
        int take = 0;
        if (last > nums[index]){
            take = 1 + memoized(nums, index - 1, nums[index], dp, maximum);
        }
        dp[index][last+maximum] = max(not_take, take);
        return dp[index][last+maximum];
    }

    int lengthOfLIS(vector<int>& nums) {
        int maximum = 0;
        for(auto num: nums){
            maximum = max(maximum, abs(num));
        }
        vector<vector<int>> dp(nums.size(), vector<int>((maximum + 2) * 2, -1));
        return memoized(nums, nums.size() - 1, maximum + 1, dp, maximum);
    }
};