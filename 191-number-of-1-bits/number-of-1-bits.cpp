class Solution {
public:
    int hammingWeight(int n) {
        int count = 0;
        for(int i = 0; i < 32; i ++){
            cout << (n &&1 << i) << endl;
            if ((n & (1 << i)) != 0){
                count += 1;
            }
        }
        return count;
    }
};