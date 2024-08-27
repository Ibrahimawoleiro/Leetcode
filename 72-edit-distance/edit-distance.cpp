class Solution {
public:
    // TC -> O(exponential)
    // SC -> O()
    int recursive(string s, string t, int i, int j){
        if(i < 0) return j + 1;
        if(j < 0) return i + 1;
        if(s[i] == t[j]){
            return recursive(s, t, i - 1, j - 1);
        }else{
            int del = recursive(s , t, i - 1, j);
            int insert = recursive(s, t, i, j - 1);
            int replace = recursive(s , t, i - 1, j - 1);

            return 1 + min(del, min(insert, replace));
        }
    }

    //O(Polynomial)
    //O(N + M + N * M)
    // int memoized(string s, string t, int i, int j,vector<vector<int>>& dp){
    //     if(i < 0) return j + 1;
    //     if(j < 0) return i + 1;
    //     if (dp[i][j] != -1){
    //         return dp[i][j];
    //     }
    //     if(s[i] == t[j]){
    //         return memoized(s, t, i - 1, j - 1, dp);
    //     }else{
    //         int del = memoized(s , t, i - 1, j, dp);
    //         int insert = memoized(s, t, i, j - 1, dp);
    //         int replace = memoized(s , t, i - 1, j - 1, dp);

    //         dp[i][j] = 1 + min(del, min(insert, replace));
    //     }
    //     return dp[i][j];
    // }
    
    // // TC -> O(Polynomial)
    // // SC -> O(N * M)
    // int tabulation(string s, string t){
    //     vector<vector<int>> dp (s.size() + 1, vector<int>(t.size() + 1, 0));
    //     for(int i = 0; i <= s.size(); i++){
    //         dp[i][0] = i;
    //     }
    //     for(int j = 0; j <= t.size(); j++){
    //         dp[0][j] = j;
    //     }
    //     for(int i = 1; i<= s.size(); i++){
    //         for(int j = 1; j <= t.size(); j++){
    //             if(s[i - 1] == t[j- 1]){
    //                 dp[i][j] = dp[i - 1][j - 1];
    //             }else{
    //                 int del = dp[i - 1][j];
    //                 int insert = dp[i][j - 1];
    //                 int replace = dp[i - 1][j - 1];
    //                 dp[i][j] = 1 + min(del, min(insert, replace));
    //             }
    //         }
    //     }
    //     return dp[s.size()][t.size()];
    // }

    // TC -> (Polynomial)
    // SC -> O(M)
    int optimizedTabulation(string s, string t){
        vector<int> prev(t.size() + 1, -1);
        vector<int> curr(t.size() + 1, -1);
        for(int j = 0; j <= t.size(); j++){
            curr[j] = j;
        }
        prev = curr;
        for(int i = 1; i<= s.size(); i++){
            curr[0] = i;
            for(int j = 1; j <= t.size(); j++){
                if(s[i - 1] == t[j- 1]){
                    curr[j] = prev[j - 1];
                }else{
                    int del = prev[j];
                    int insert = curr[j - 1];
                    int replace = prev[j - 1];
                    curr[j] = 1 + min(del, min(insert, replace));
                }
            }
            prev = curr;
        }
        return prev[t.size()];
    }

    int minDistance(string word1, string word2) {
        return optimizedTabulation(word1, word2);
    }
};