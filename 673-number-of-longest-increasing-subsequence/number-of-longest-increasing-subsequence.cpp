class Solution {
public:
    int tabulation(vector<int>& nums) {
    if (nums.empty()) return 0;

    vector<int> lis_count(nums.size(), 1);
    vector<int> lis_length(nums.size(), 1);
    
    for (int index = 0; index < nums.size(); index++) {
        for (int s = index - 1; s >= 0; s--) {
            if (nums[s] < nums[index]) {
                if (lis_length[s] + 1 > lis_length[index]) {
                    lis_length[index] = lis_length[s] + 1;
                    lis_count[index] = lis_count[s];
                } else if (lis_length[s] + 1 == lis_length[index]) {
                    lis_count[index] += lis_count[s];
                }
            }
        }
    }

    int maximum = *max_element(lis_length.begin(), lis_length.end());
    int ans = 0;
    
    for (int index = 0; index < nums.size(); index++) {
        if (lis_length[index] == maximum) {
            ans += lis_count[index];
        }
    }
    
    return ans;
}
    int findNumberOfLIS(vector<int>& nums) {
        return tabulation(nums);
    }
};