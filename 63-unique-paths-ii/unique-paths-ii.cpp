class Solution {
public:
    // // TC -> O(N * C * 2 ^ N)
    // // SC -> O(N + M)
    // int recursive(int r, int c, vector<vector<int>>& grid){
    //     //base case
    //     if (r < 0 or c < 0 or grid[r][c] == 1){
    //         return 0;
    //     }
    //     if (r == 0 && c == 0){
    //         return 1;
    //     }
    //     //recursive step
    //     int left = 0;
    //     int up = 0;
    //     left = recursive(r, c - 1, grid);
    //     up = recursive(r - 1, c, grid);
    //     return left + up;
    // }

    // // TC -> O(N * M)
    // // SC -> O(N + M + (N * M))
    // int memoized(vector<vector<int>>& grid, vector<vector<int>>& dp, int r, int c){
    //     // base case
    //     if (r < 0 || c < 0 || grid[r][c] == 1){
    //         return 0;
    //     }
    //     if (r == 0 && c == 0){
    //         return 1;
    //     }
    //     if (dp[r][c] != -1){
    //         return dp[r][c];
    //     }
    //     // recursive case
    //     int left = memoized(grid, dp, r, c - 1);
    //     int up = memoized(grid, dp, r - 1, c);
    //     dp[r][c] = left + up;
    //     return dp[r][c];
    // }

    int tabulation(vector<vector<int>>& grid){
        vector<vector<int>> dp(grid.size(), vector<int>(grid[0].size(), -1));
        for(int r = 0; r < grid.size(); r++){
            for(int c = 0; c < grid[0].size(); c++){
                if (grid[r][c] == 1){
                    dp[r][c] = 0;
                    continue;
                }
                if (r == 0 && c == 0){
                    dp[r][c] = 1;
                    continue;
                }
                int left = 0;
                int up = 0;
                if (c - 1 >= 0){
                    left = dp[r][c - 1];
                }
                if (r - 1 >= 0){
                    up = dp[r - 1][c];
                }
                dp[r][c] = left + up;
            }
        }
        return dp[grid.size() - 1][grid[0].size() - 1];
    }
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        return tabulation(obstacleGrid);
    }
};