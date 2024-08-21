class Solution {
public:
    // // TC -> O(2 ^ N)
    // // SC -> O(path)
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

    int memoized(int r, int c, vector<vector<int>>& dp){
        if (r < 0 || c < 0){
            return 0;
        }
        if (r == 0 and c == 0){
            return 1;
        }

        if (dp[r][c] != -1){
            return dp[r][c];
        }

        int left = memoized(r , c - 1, dp);
        int up = memoized(r - 1, c, dp);

        dp[r][c] = left + up;

        return dp[r][c];
    }

    int uniquePaths(int m, int n) {
        vector<vector<int>> dp(m, vector<int>(n, -1));
        return memoized(m - 1, n - 1, dp);
    }
};