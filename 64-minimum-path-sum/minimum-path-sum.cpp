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

    // // TC -> O(N * M * 2)
    // // SC -> O(N * M + (N + M))
    // int memoized(vector<vector<int>>& grid, vector<vector<int>>& dp, int r, int c){
    //     if (r < 0 || c < 0){
    //         return 100000000;
    //     }
    //     if (r == 0 and c == 0){
    //         return grid[r][c];
    //     }
    //     if (dp[r][c] != -1){
    //         return dp[r][c];
    //     }
    //     int left = grid[r][c] + memoized(grid, dp , r, c - 1);
    //     int up = grid[r][c] + memoized(grid, dp , r - 1 , c);
    //     dp[r][c] = min(left , up);
    //     return dp[r][c];
    // }

    // // TC -> O(N * M * 2)
    // // SC -> O(N * M)
    // int tabulation(vector<vector<int>>& grid){
    //     vector<vector<int>> dp(grid.size(), vector<int>(grid[0].size(), -1));
    //     for (int r = 0; r < grid.size(); r++){
    //         for (int c = 0; c < grid[0].size(); c++){
    //             if (r == 0 && c == 0){
    //                 dp[r][c] = grid[0][0];
    //                 continue;
    //             }
    //             int left = 100000000;
    //             int up = 1000000000;
    //             if (c - 1 >= 0){
    //                 left = dp[r][c - 1];
    //             }
    //             if (r - 1 >= 0){
    //                 up = dp[r - 1][c];
    //             }
    //             dp[r][c] = grid[r][c] + min(up, left);
    //         }
    //     }
    //     return dp[grid.size() - 1][grid[0].size() - 1];
    // }

    // TC -> O(N * M)
    // SC -> O(M)
    int optimizedTabulation(vector<vector<int>>& grid){
        vector<int> prev(grid[0].size(), -1);
        vector<int> curr(grid[0].size(), -1);
        for (int r = 0; r < grid.size(); r++){
            for(int c = 0; c < grid[0].size(); c++){
                if (r == 0 && c == 0){
                    curr[c] = grid[r][c];
                    continue;
                }
                int left = 100000000;
                int up = 100000000;
                if (c - 1 >= 0){
                    left = curr[c - 1];
                }
                if (r - 1 >= 0){
                    up = prev[c];
                }
                curr[c] = grid[r][c] + min(up, left);
            }
            prev = curr;
            curr = vector<int>(grid[0].size(), -1);
        }
        return prev[grid[0].size() - 1];
    }
    
    int minPathSum(vector<vector<int>>& grid) {
        return optimizedTabulation(grid);
    }
};