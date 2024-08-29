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

    // int memoized(vector<int>& nums, int index, int last, vector<vector<int>>& dp, int maximum){
    //     if (index == 0){
    //         if (last > nums[index]) return 1;
    //         return 0;
    //     }
    //     if(dp[index][last+maximum] != -1){
    //         return dp[index][last+maximum];
    //     }
    //     int not_take = memoized(nums, index - 1, last, dp, maximum);
    //     int take = 0;
    //     if (last > nums[index]){
    //         take = 1 + memoized(nums, index - 1, nums[index], dp, maximum);
    //     }
    //     dp[index][last+maximum] = max(not_take, take);
    //     return dp[index][last+maximum];
    // }

    int tabulation(vector<int>& nums){
        int maximum = 0;
        int minimum = INT_MAX;
        for(auto num: nums){
            maximum = max(maximum, abs(num));
            minimum = min(minimum, num);
        }
        vector<vector<int>> dp(nums.size(), vector<int>((maximum + 2) * 2, 0));
        for(int index = 0; index < nums.size(); index++){
            for(int last = minimum; last <= maximum + 1; last++){
                if(index == 0){
                    if(last  > nums[index]){
                        dp[index][last + maximum] = 1;
                    }
                }else{
                    int not_take = dp[index - 1][last+maximum];
                    int take = 0;
                    if (last > nums[index]){
                        take = 1 + dp[index - 1][nums[index] + maximum];
                    }
                    dp[index][last + maximum] = max(take, not_take);
                }
            }
        }
        return dp[nums.size() - 1][maximum + 1 + maximum];
    }

    int lengthOfLIS(vector<int>& nums) {
        return tabulation(nums);
    }
};