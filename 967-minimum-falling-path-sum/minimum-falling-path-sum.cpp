class Solution {
public:
    // // TC -> O(N * M * 3 ^ N)
    // // SC -> O(N)
    // int recursive(vector<vector<int>>& matrix, int r, int c){
    //     if (c < 0 || c >= matrix[0].size()){
    //         return INT_MAX;
    //     }
    //     int row_size = matrix.size();
    //     int col_size = matrix[0].size();
    //     if (r == row_size - 1){
    //         return matrix[r][c];
    //     }
    //     int left = recursive(matrix, r + 1, c - 1);
    //     int right = recursive(matrix, r + 1, c + 1);
    //     int below = recursive(matrix, r + 1, c);
    //     int minimum = matrix[r][c] + min(min(left, right), below);
    //     return minimum;
    // }

    // // TC -> O(N * M * 3N)
    // // sc -> O(N * M + N)
    // int memoization(vector<vector<int>>& matrix,vector<vector<int>>& dp, int r, int c){
    //     if (c < 0 || c >= matrix[0].size()){
    //         return INT_MAX;
    //     }
    //     int row_size = matrix.size();
    //     int col_size = matrix[0].size();
    //     if (r == row_size - 1){
    //         return matrix[r][c];
    //     }
    //     if (dp[r][c] != -1){
    //         return dp[r][c];
    //     }
    //     int left = memoization(matrix, dp, r + 1, c - 1);
    //     int right = memoization(matrix, dp, r + 1, c + 1);
    //     int below = memoization(matrix, dp, r + 1, c);
    //     int minimum = matrix[r][c] + min(min(left, right), below);
    //     dp[r][c] = minimum;
    //     return minimum;
    // }

    int tabulation(vector<vector<int>>& matrix){
        int row_size = matrix.size();
        int col_size = matrix[0].size();
        vector<vector<int>> dp(row_size, vector<int>(col_size, -1));
        int ans;
        for (int r = row_size - 1; r >= 0; r--){
            ans = INT_MAX;
            for (int c = 0; c < col_size; c++){
                if (r == row_size - 1){
                    dp[r][c] = matrix[r][c];
                    ans = min(ans, dp[r][c]);
                    continue;
                } 

                int left = INT_MAX;
                int right = INT_MAX;
                int below = INT_MAX;

                if (c - 1 >= 0){
                    left = dp[r + 1][c - 1];
                }
                if (c + 1 < col_size){
                    right = dp[r + 1][c + 1];
                }
                below = dp[r + 1][c];
                dp[r][c] = matrix[r][c] + min(min(left, right), below);
                ans = min(ans, dp[r][c]);
            }
        }
        return ans;
    }
    int minFallingPathSum(vector<vector<int>>& matrix) {
        return tabulation(matrix);
    }
};