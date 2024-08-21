class Solution {
public:
    // // TC -> O(N * M * 2 ^ N)
    // // SC -> O(N + M)
    // int recursive(vector<vector<int>>& grid, int r, int c){
    //     if (r < 0 || c < 0){
    //         return 1000000000;
    //     }
    //     if (r == 0 && c == 0){
    //         return grid[r][c];
    //     }
    //     int left = grid[r][c] + recursive(grid, r, c - 1);
    //     int up = grid[r][c] + recursive(grid, r - 1 , c);
    //     return min(left, up);
    // }


    int memoized(vector<vector<int>>& grid, vector<vector<int>>& dp, int r, int c){
        if (r < 0 || c < 0){
            return 100000000;
        }

        if (r == 0 and c == 0){
            return grid[r][c];
        }

        if (dp[r][c] != -1){
            return dp[r][c];
        }

        int left = grid[r][c] + memoized(grid, dp , r, c - 1);
        int up = grid[r][c] + memoized(grid, dp , r - 1 , c);
        dp[r][c] = min(left , up);
        return dp[r][c];
    }
    int minPathSum(vector<vector<int>>& grid) {
        vector<vector<int>> dp(grid.size(), vector<int>(grid[0].size(), -1));
        return memoized(grid,dp, grid.size() - 1, grid[0].size() - 1);
    }
};