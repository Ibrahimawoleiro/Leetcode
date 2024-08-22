class Solution {
    // // TC -> O(N * 2 ^ N);
    // // SC -> O(N)
    // public boolean recursion(int[] nums, int index, int remainder){
    //     if (remainder < 0){
    //         return false;
    //     }
    //     if (index == 0){
    //         if (nums[index] == remainder){
    //             return true;
    //         }else{
    //             return false;
    //         }
    //     }

    //     boolean take = recursion(nums,index - 1, remainder - nums[index]);
    //     boolean not_take = recursion(nums, index - 1, remainder);

    //     return take || not_take;
    // }

    public boolean memoized(int[] nums, Boolean[][] dp, int index, int remainder){
        if (remainder < 0){
            return false;
        }
        if (index == 0){
            if (nums[index] == remainder){
                return true;
            }else{
                return false;
            }
        }
        if(dp[index][remainder] != null){
            return dp[index][remainder];
        }

        boolean take = memoized(nums, dp, index - 1, remainder - nums[index]);
        boolean not_take = memoized(nums,dp, index - 1, remainder);

        dp[index][remainder] = take || not_take;
        return dp[index][remainder];
    }

    public boolean canPartition(int[] nums) {
        int total = 0;
        for(int num : nums){
            total += num;
        }
        if (total % 2 == 1){
            return false;
        }
        int arr_size = nums.length;
        Boolean[][] dp = new Boolean[arr_size][total];
        for (int r = 0; r < arr_size; r++){
            for (int c = 0; c < total; c++){
                dp[r][c] = null;
            }
        }
        return memoized(nums, dp, nums.length - 1, total / 2);
    }
}