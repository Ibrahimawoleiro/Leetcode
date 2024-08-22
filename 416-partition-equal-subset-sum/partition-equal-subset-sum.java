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

    // TC -> O(N * TOTAL * 2)
    // SC -> O(N * TOTAL + N)
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

    boolean tabulation(int[] nums){
        int total = 0;
        for(int num : nums){
            total += num;
        }
        if (total % 2 == 1){
            return false;
        }
        int arr_size = nums.length;
        Boolean[][] dp = new Boolean[arr_size][total + 1];
        for (int index = 0; index < arr_size; index++){
            for (int c = 0; c < total + 1; c++){
                if (index == 0 && nums[index] == c){
                    dp[index][c] = true;
                    continue;
                }
                boolean not_take = dp[index - 1][c];
                boolean take = nums[index] == c ? true : false; 
                if (!take && c - nums[index] >= 0){
                    take = dp[index][c - nums[index]];
                }
                dp[index][c] = take || not_take;
            }
        }
        return dp[arr_size - 1][total];
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
        return memoized(nums, dp, nums.length - 1, total / 2);
    }
}