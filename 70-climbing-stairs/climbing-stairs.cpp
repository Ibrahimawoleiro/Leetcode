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

    // Memoization function
    // TC -> O(N)
    // SC -> O(N)
    // int memoization(int n , vector<int>& dp){
    //     if (n == 0 || n == 1){
    //         return 1;
    //     }
    //     if (dp[n] != -1){
    //         return dp[n];
    //     }
        
    //     int curr = memoization(n - 1, dp) + memoization(n - 2, dp);

    //     dp[n] = curr;

    //     return curr;
    // }

    // Tabulation function
    // TC -> O(N)
    // SC -> O(N)
    // int tabulation(int n){
    //     vector<int> tab(n + 1, 0);
    //     tab[0] = 1;
    //     tab[1] = 1;

    //     for(int i = 2; i <= n; i++){
    //         tab[i] = tab[i - 1] + tab[i - 2];
    //     }
    //     return tab[n];
    // }

    // OptimizedTabulation function
    // TC -> O(N)
    // SC -> O(1)

    int opt_tabulation(int n){
        int prev = 1;
        int curr = 1;

        for (int i = 2; i <= n; i ++){
            int next = curr + prev;
            prev = curr;
            curr = next;
        }
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

        return opt_tabulation(n);
    }
};