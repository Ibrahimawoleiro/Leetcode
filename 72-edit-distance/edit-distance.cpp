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

    int memoized(string s, string t, int i, int j,vector<vector<int>>& dp){
        if(i < 0) return j + 1;
        if(j < 0) return i + 1;
        if (dp[i][j] != -1){
            return dp[i][j];
        }
        if(s[i] == t[j]){
            return memoized(s, t, i - 1, j - 1, dp);
        }else{
            int del = memoized(s , t, i - 1, j, dp);
            int insert = memoized(s, t, i, j - 1, dp);
            int replace = memoized(s , t, i - 1, j - 1, dp);

            dp[i][j] = 1 + min(del, min(insert, replace));
        }
        return dp[i][j];
    }

    int minDistance(string word1, string word2) {
        vector<vector<int>> dp (word1.size(), vector<int>(word2.size(), -1));
        return memoized(word1, word2, word1.size() - 1, word2.size() - 1, dp);
    }
};