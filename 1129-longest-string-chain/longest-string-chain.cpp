class Solution {
public:
    bool canform( string& a, string& b){
        if(a.size() + 1 != b.size()) return false;
        int i = 0;
        int j = 0;
        while (i < a.size() && j < b.size()){
            if (a[i] == b[j]){
                i++;
                j++;
            }else{
                j++;
            }
        }
        return i == a.size();
    }
    // int recursive(vector<string>& words, int index, int last_index){
    //     cout << index << " "<< last_index << endl;
    //     if (index < 0){
    //         return 0;
    //     }
    //     int not_take = recursive(words, index - 1, last_index);
    //     int take = 0;
    //     if (last_index == words.size() || canform(words[index], words[last_index])){
    //         take = 1 + recursive(words, index - 1, index);
    //     }
    //     return max(take, not_take);
    // }

    int memoized(vector<string>& words, int index, int last_index, vector<vector<int>>& dp){
        if (index < 0){
            return 0;
        }
        if(dp[index][last_index] != -1){
            return dp[index][last_index];
        }
        int not_take = memoized(words, index - 1, last_index, dp);
        int take = 0;
        if (last_index == words.size() || canform(words[index], words[last_index])){
            take = 1 + memoized(words, index - 1, index, dp);
        }
        return max(take, not_take);
    }

    int tabulation(vector<string> & words){
        vector<int> chain_length(words.size(), 1);
        for(int index = 0; index < words.size(); index++){
            for(int s = index - 1; s >= 0; s --){
                if(canform(words[s], words[index])){
                    chain_length[index] = max(chain_length[index],chain_length[s] + 1);

                }
            }
        }
        int maximum = 0;
        for(auto num: chain_length){
            maximum = max(maximum, num);
        }
        return maximum;
    }

    static bool comp(string& a, string& b){
        return a.size() < b.size();
    }

    int longestStrChain(vector<string>& words) {
        sort(words.begin(), words.end(),comp);
        vector<vector<int>> dp(words.size(), vector<int>(words.size() + 1, -1));
        return tabulation(words);
    }
};