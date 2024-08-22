class Solution {
public:

    // // TC -> O(N * M * 2 ^ N)
    // // SC -> O(N)
    // int recursive(vector<vector<int>>& triangle, int r, int c){
    //     int row_size = triangle.size();
    //     int col_size = triangle[0].size();
    //     if (r == row_size - 1){
    //         return triangle[r][c];
    //     }
    //     int below = recursive(triangle, r + 1, c);
    //     int diagonal = recursive(triangle, r + 1, c + 1);
    //     int minimum = min(below, diagonal);
    //     return triangle[r][c] + minimum;
    // }

    // // TC -> O(N * M * 2)
    // // SC -> O(N * M + N)
    // int memoized(vector<vector<int>>& triangle, vector<vector<int>>& dp , int r, int c){
    //     int row_size = triangle.size();
    //     int col_size = triangle[0].size();
    //     if (r == row_size - 1){
    //         return triangle[r][c];
    //     }
    //     if (dp[r][c] != -1){
    //         return dp[r][c];
    //     }
    //     int below = recursive(triangle, r + 1, c);
    //     int diagonal = recursive(triangle, r + 1, c + 1);
    //     int minimum = min(below, diagonal);
    //     dp[r][c] =  triangle[r][c] + minimum;
    //     return dp[r][c];
    // }

    // // TC -> O(N * M)
    // // SC -> O(N * M)
    // int tabulation(vector<vector<int>>& triangle){
    //     int row_size = triangle.size();
    //     int col_size = triangle[triangle.size() - 1].size();
    //     vector<vector<int>> dp(row_size, vector<int>(col_size, INT_MAX));
    //     int min_path;
    //     for (int r = 0; r < row_size; r++){
    //         min_path = INT_MAX;
    //         for (int c = 0; c < col_size; c++){
    //             if (r == 0 && c == 0){
    //                 dp[r][c] = triangle[r][c];
    //                 min_path = dp[r][c];
    //                 continue;
    //             }
    //             int upper = INT_MAX;
    //             int diagonal = INT_MAX;
    //             if (c >= triangle[r].size()) break;
    //             if (r - 1 >= 0){
    //                 upper = dp[r - 1][c];
    //                 if (c - 1 >= 0){
    //                     diagonal = dp[r - 1][c - 1];
    //                 }
    //             }
    //             int minimum = min(upper, diagonal);
    //             dp[r][c] = triangle[r][c] + minimum;
    //             (dp[r][c] < min_path)? min_path = dp[r][c]: min_path;
    //         }
    //     }
    //     return min_path;
    // }

    int optimizedTabulation(vector<vector<int>>& triangle){
        int row_size = triangle.size();
        int col_size = triangle[triangle.size() - 1].size();
        vector<vector<int>> prev(1, vector<int>(col_size, INT_MAX));
        vector<vector<int>> curr(1, vector<int>(col_size, INT_MAX));
        int min_path;
        for (int r = 0; r < row_size; r++){
            min_path = INT_MAX;
            for (int c = 0; c < col_size; c++){
                if (r == 0 && c == 0){
                    curr[r][c] = triangle[r][c];
                    min_path = curr[0][0];
                    continue;
                }
                int upper = INT_MAX;
                int diagonal = INT_MAX;
                if (c >= triangle[r].size()) break;
                if (r - 1 >= 0){
                    upper = prev[0][c];
                    if (c - 1 >= 0){
                        diagonal = prev[0][c - 1];
                    }
                }
                int minimum = min(upper, diagonal);
                curr[0][c] = triangle[r][c] + minimum;
                (curr[0][c] < min_path)? min_path = curr[0][c]: min_path;
            }
            prev = curr;
        }
        return min_path;
    }

    int minimumTotal(vector<vector<int>>& triangle) {
        return optimizedTabulation(triangle);
    }
};