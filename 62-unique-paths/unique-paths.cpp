class Solution {
public:
    // // TC -> O(2 ^ N)
    // // SC -> O(N + M)
    // int recursive(int r, int c){
    //     if (r < 0 or c < 0){
    //         return 0;
    //     }
    //     if (r == 0 and c == 0){
    //         return 1;
    //     }
    //     int left = recursive(r, c-1);
    //     int up = recursive(r - 1, c);

    //     return left + up;
    // }

    // // TC -> O(N * M)
    // // SC -> O((N + M) * (N * M))
    // int memoized(int r, int c, vector<vector<int>>& dp){
    //     if (r < 0 || c < 0){
    //         return 0;
    //     }
    //     if (r == 0 and c == 0){
    //         return 1;
    //     }

    //     if (dp[r][c] != -1){
    //         return dp[r][c];
    //     }

    //     int left = memoized(r , c - 1, dp);
    //     int up = memoized(r - 1, c, dp);

    //     dp[r][c] = left + up;

    //     return dp[r][c];
    // }

    // // TC -> O(N * M)
    // // SC -> O(N * M)
    // int tabulation(int m, int n){
    //     vector<vector<int>> dp(m, vector<int>(n, -1));  
    //     for(int r = 0; r < m; r++){
    //         for (int c = 0; c < n; c++){
    //             if (r == 0 and c == 0){
    //                 dp[r][c] = 1;
    //                 continue;
    //             }
    //             int left = 0;
    //             int up = 0;

    //             if (c - 1 >= 0){
    //                 left = dp[r][c - 1];
    //             }
    //             if (r - 1 >= 0){
    //                 up = dp[r - 1][c];
    //             }
    //             dp[r][c] = left + up;
    //          }
    //     }
    //     return dp[m - 1][n - 1];
    // }

    int optimizedTabulation(int m, int n){
        vector<vector<int>> prev(1, vector<int>(n, -1));  
        vector<vector<int>> curr(1, vector<int>(n, -1));

        for (int r = 0; r < m; r++){
            for (int c = 0; c < n; c ++){
                if (r == 0 and c == 0){
                    curr[0][0] = 1;
                    continue;
                }
                int left = 0;
                int up = 0;

                if (c - 1 >= 0){
                    left = curr[0][c - 1];
                }
                if (r - 1 >= 0){
                    up = prev[0][c];
                }
                curr[0][c] = left + up;
            }
            prev = curr;
            curr = vector<vector<int>>(1, vector<int>(n, -1));
        } 
        return prev[0][n - 1];
    }

    int uniquePaths(int m, int n) {
        return optimizedTabulation(m, n);
    }
};