class Solution {
public:
    int recursive_lcs(string s, string t,int i, int j, vector<vector<int>>& dp){
        if(i < 0 || j < 0){
            return 0;
        }
        if(s[i] == t[j]){
            return 1 + recursive_lcs(s, t, i - 1, j - 1, dp);
        }else{
            return max(recursive_lcs(s,t,i - 1, j,dp), recursive_lcs(s,t,i, j - 1,dp));
        }
    }

    string scs(string s, string t){
        vector<vector<int>> dp(s.size() + 1, vector<int>(t.size() + 1, -1));
        for(int i = 0; i <= s.size(); i++){
            dp[i][0] = 0;
        }
        for(int j = 0; j <= t.size(); j++){
            dp[0][j] = 0;
        }
        for(int i = 1; i <= s.size(); i++){
            for(int j = 1; j <= t.size(); j++){
                if (s[i - 1] == t[j - 1]){
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                }else{
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]);
                }
            }
        }
        // for(int i = 0; i <= s.size(); i++){
        //     for(int j = 0; j <= t.size(); j++){
        //         cout << dp[i][j] << " ";
        //     }
        //     cout << endl;
        // }
        int i = s.size();
        int j = t.size();
        string ans = "";
        while(i > 0 || j > 0){
            if (i > 0 && j > 0){
                if(s[i - 1] == t[j - 1]){
                    ans += s[i - 1];
                    i -= 1;
                    j -= 1;
                }else{
                    if (dp[i - 1][j] == dp[i][j]){
                        ans += s[i - 1];
                        i -= 1;
                    }else if(dp[i][j - 1] == dp[i][j]){
                        ans += t[j - 1];
                        j -= 1;
                    }else{
                        ans += s[i - 1];
                        i -= 1;
                    }
                }
            }else{
                if(i > 0){
                    ans += s[i - 1];
                        i -= 1;
                }else{
                    ans += t[j - 1];
                        j -= 1;
                }
            }
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
    string shortestCommonSupersequence(string str1, string str2) {
        // vector<vector<int>> dp(str1.size() + 1, vector<int>(str2.size() + 1, -1));
        return scs(str1, str2);
    }
};