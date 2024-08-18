class Solution {
public:
    //Recursive function
    // int helper(int n){
    //     if (n == 0){
    //         return 1;
    //     }
    //     if (n == 1){
    //         return 1;
    //     }
    //     return helper(n - 1) + helper(n - 2);
    // }

    //Memoization fuction

    int memoization(int n , vector<int>& dp){
        if (n == 0 || n == 1){
            return 1;
        }
        if (dp[n] != -1){
            return dp[n];
        }
        
        int curr = memoization(n - 1, dp) + memoization(n - 2, dp);

        dp[n] = curr;

        return curr;
    }


    int climbStairs(int n) {
        /*
        The number of ways to get to a position is 
        the number of ways to get to position - 1 
        plus
        the number of ways to get to position - 2
        why? 
        You can only get to current position from last 2 step or last step.
        */

        vector<int> dp(n + 1, -1);
        return memoization(n, dp);
    }
};