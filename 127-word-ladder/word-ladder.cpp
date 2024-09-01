class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        queue<pair<string,int>> q;
        set<string> st(wordList.begin(), wordList.end());
        q.push({beginWord, 1});
        while(!q.empty()){
            string curr = q.front().first;
            int count = q.front().second;
            string copy = curr;
            if (curr == endWord){
                return count;
            }
            q.pop();
            for(int index = 0; index < curr.size(); index++){
                for(char c = 'a'; c <='z'; c++){
                    copy[index] = c;
                    if(st.find(copy) != st.end()){
                        q.push({copy, count+ 1});
                        st.erase(copy);
                    }
                    copy = curr;
                }
            }
        }
        return 0;
    }
};