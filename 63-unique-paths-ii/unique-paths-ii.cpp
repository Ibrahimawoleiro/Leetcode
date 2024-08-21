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

    int memoized(vector<vector<int>>& grid, vector<vector<int>>& dp, int r, int c){
        // base case
        if (r < 0 || c < 0 || grid[r][c] == 1){
            return 0;
        }
        if (r == 0 && c == 0){
            return 1;
        }
        if (dp[r][c] != -1){
            return dp[r][c];
        }
        // recursive case
        int left = memoized(grid, dp, r, c - 1);
        int up = memoized(grid, dp, r - 1, c);
        dp[r][c] = left + up;
        return dp[r][c];
    }
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        vector<vector<int>> dp(obstacleGrid.size(), vector<int>(obstacleGrid[0].size(), -1));
        return memoized(obstacleGrid, dp, obstacleGrid.size() - 1, obstacleGrid[0].size() - 1);
    }
};