class Solution {
public:
    // // TC -> 0(N * M * 2 ^ N * 2 ^ M)
    // // SC -> O(N + M)
    // int recursive(int i, int j, string text1, string text2){
    //     if (i < 0 || j < 0){
    //         return 0;
    //     }
    //     if(text1[i] == text2[j]){
    //         return 1 + recursive(i - 1, j - 1, text1, text2);
    //     }else{
    //         return 0 + max(recursive(i - 1, j, text1, text2), recursive(i, j - 1, text1, text2));
    //     }
    // }

    // // TC -> 0(N * M * 2 * 2)
    // // SC -> O(N + M)
    // int memoized(int i, int j, string text1, string text2, vector<vector<int>>& dp){
    //     if (i < 0 || j < 0){
    //         return 0;
    //     }
    //     if (dp[i][j] != -1){
    //         return dp[i][j];
    //     }
    //     if(text1[i] == text2[j]){
    //         dp[i][j] = 1 + memoized(i - 1, j - 1, text1, text2, dp);
    //     }else{
    //         dp[i][j] = 0 + max(memoized(i - 1, j, text1, text2, dp), memoized(i, j - 1, text1, text2, dp) );
    //     }
    //     return dp[i][j];
    // }

    // // TC -> O(N * M * 2 * 2)
    // // SC -> O(N * M)
    // int tabulation(int i, int j, string text1, string text2){
    //     vector<vector<int>> dp(text1.size()+1, vector<int>(text2.size()+1, -1));
    //     int text1_size = text1.size();
    //     int text2_size = text2.size();
    //     for(int i = 0; i <= text1_size; i++){
    //         dp[i][0] = 0;
    //     }
    //     for(int j = 0; j <= text2_size; j++){
    //         dp[0][j] = 0;
    //     }
    //     for (int i = 1; i <= text1_size; i++){
    //         for(int j = 1; j <= text2_size; j++){
    //             if (text1[i - 1] == text2[j - 1]){
    //                 dp[i][j] = 1 + dp[i - 1][j - 1];
    //             }else{
    //                 dp[i][j] = 0 + max(dp[i - 1][j], dp[i][j-1]);
    //             }
    //         }
    //     }
    //     return dp[text1_size][text2_size];
    // }

    // TC -> O(N * M * 2 * 2)
    // SC -> O(M)
    int optimizedTabulation(int i, int j, string text1, string text2){
        vector<int> prev(text2.size()+1, 0);
        vector<int> curr(text2.size()+1, 0);
        int text1_size = text1.size();
        int text2_size = text2.size();
            curr[0] = 0;
        for(int j = 0; j <= text2_size; j++){
            curr[j] = 0;
        }
        for (int i = 1; i <= text1_size; i++){
            for(int j = 1; j <= text2_size; j++){
                if (text1[i - 1] == text2[j - 1]){
                    curr[j] = 1 + prev[j - 1];
                }else{
                    curr[j] = 0 + max(prev[j], curr[j-1]);
                }
            }
            prev = curr;
        }
        return prev[text2_size];
    }

    int longestCommonSubsequence(string text1, string text2) { 
        return optimizedTabulation(text1.size() - 1, text2.size() - 1, text1, text2);
    }
};