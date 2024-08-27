class Solution {
public:
    // // TC -> O(N * M * 2 ^ (M + N))
    // // SC -> O(N + M)
    // int recursive(string s, string t, int i, int j){
    //     if (j < 0) return 1;
    //     if (i < 0) return 0;

    //     if (s[i] == t[j]){
    //         return recursive(s, t, i - 1, j - 1) + recursive(s, t, i - 1, j);
    //     }else{
    //         return recursive(s,t,i - 1, j);
    //     }
    // }

    int memoized(string s, string t, int i, int j, vector<vector<int>>& dp){
        if (j < 0) return 1;
        if (i < 0) return 0;

        if (dp[i][j] != -1){
            return dp[i][j];
        }
        if (s[i] == t[j]){
            dp[i][j] = memoized(s, t, i - 1, j - 1, dp) + memoized(s, t, i - 1, j, dp);
        }else{
            dp[i][j] = memoized(s,t,i - 1, j, dp);
        }
        return dp[i][j];
    }

    int numDistinct(string s, string t) {
        vector<vector<int>> dp(s.size(), vector<int>(t.size(), -1));
        return memoized(s, t, s.size() - 1, t.size() - 1, dp);
    }
};