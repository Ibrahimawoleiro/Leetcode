class Solution {
public:

    // bool recursive(string p, string s,  int i, int j){
    //     if (i < 0 && j < 0) return true;
    //     if (i < 0) return false;
    //     if (j < 0){
    //         bool valid = false;
    //         for(int k = 0; k <= i; k++){
    //             if (p[k] != '*'){
    //                 return valid;
    //             }
    //         }
    //         valid = true;
    //         return valid;
    //     }
    //     if(p[i] == '?' || p[i] == s[j]){
    //         return recursive(p, s, i - 1, j - 1);
    //     }else{
    //         if (p[i] == '*'){
    //             return recursive(p, s, i, j - 1) || recursive(p, s, i - 1, j - 1) || recursive(p, s, i - 1, j);
    //         }else{
    //             return false;
    //         }
    //     }
    // }

    // bool memoized(string p, string s,  int i, int j, vector<vector<int>>& dp){
    //     if (i < 0 && j < 0) return true;
    //     if (i < 0) return false;
    //     if (j < 0){
    //         bool valid = false;
    //         for(int k = 0; k <= i; k++){
    //             if (p[k] != '*'){
    //                 return valid;
    //             }
    //         }
    //         valid = true;
    //         return valid;
    //     }
    //     if(dp[i][j] != -1){
    //         return dp[i][j];
    //     }
    //     if(p[i] == '?' || p[i] == s[j]){
    //         dp[i][j] = memoized(p, s, i - 1, j - 1,dp);
    //     }else{
    //         if (p[i] == '*'){
    //             dp[i][j] = memoized(p, s, i, j - 1,dp) || memoized(p, s, i - 1, j - 1,dp) || memoized(p, s, i - 1, j,dp);
    //         }else{
    //             dp[i][j] = false;
    //         }
    //     }
    //     return dp[i][j];
    // }

    bool tabulation(string s, string p){
        vector<vector<int>> dp(p.size() + 1, vector<int>(s.size() + 1, -1));
        dp[0][0] = true;
        for(int j = 1; j <= s.size(); j++){
            dp[0][j] = false;
        }
        for(int i = 1; i <= p.size(); i++){
            if (p[i - 1] != '*' || dp[i - 1][0] == false){
                dp[i][0] = false;
            }else{
                dp[i][0] = true;
            }
        }
        for(int i = 1; i<= p.size(); i++){
            for(int j = 1; j<= s.size(); j++){
                if(p[i - 1] == '?' || p[i - 1] == s[j - 1]){
                    dp[i][j] = dp[i - 1][j - 1];
                }else{
                    if(p[i - 1] == '*'){
                        dp[i][j] = dp[i][j - 1] || dp[i - 1][j - 1] || dp[i - 1][j];
                    }else{
                        dp[i][j] = false;
                    }
                }
            }
        }
        return dp[p.size()][s.size()];
    }

    bool isMatch(string s, string p) {
        vector<vector<int>> dp(p.size(), vector<int>(s.size(), -1));
        return tabulation(s, p);
    }
};