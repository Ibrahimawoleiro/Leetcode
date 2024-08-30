class Solution {
public:
    // vector<int> recursive(vector<int>& nums, int index, vector<int>& combination, vector<int>){
    //     if (index == nums.size() - 1){
    //         int comb_last_index = combination.size() - 1;
    //         if (combination.size() > 0 && (nums[index] % combination[comb_last_index] == 0)){
    //             vector<int> take = combination;
    //             take.push_back(nums[index]);
    //             return take;
    //         }else if(combination.size() == 0){
    //             return vector<int>{nums[nums.size() - 1]};
    //         }else{
    //             return combination;
    //         }
    //     }
    //     vector<int> not_take = recursive(nums, index + 1, combination);
    //     vector<int> take = combination;
    //     if (combination.size() > 0){
    //         int comb_last_index = combination.size() - 1;
    //         if (nums[index] % combination[comb_last_index] == 0){
    //             take = combination;
    //             take.push_back(nums[index]);
    //             take = recursive(nums, index + 1, take);
    //         }
    //     }else{
    //         take.push_back(nums[index]);
    //         take = recursive(nums, index + 1, take);
    //     }
    //     if(not_take.size() > take.size()) return not_take;
    //     return take;
    // }

    vector<int> tabulation(vector<int>& nums){
        vector<int> subset_size_tracker(nums.size(), 1);
        vector<int> prev_tracker(nums.size());
        iota(prev_tracker.begin(), prev_tracker.end(), 0);
        for (int index = 0; index < nums.size(); index++){
            for(int j = index - 1; j>=0; j--){
                if(nums[index] % nums[j] == 0){
                    if (!(subset_size_tracker[j] + 1 > subset_size_tracker[index])) continue;
                    prev_tracker[index] = j;
                    subset_size_tracker[index] = subset_size_tracker[j] + 1;
                }
            }
        }
        vector<int> ans;
        int max_index = -1;
        int size = -1;
        for(auto val: subset_size_tracker){
            cout << val << " "<< endl;
        }
        for(int index = 0; index < nums.size(); index++){
            if(subset_size_tracker[index] > size){
                size = subset_size_tracker[index];
                max_index = index;
            }
        }
        while(true){
            ans.push_back(nums[max_index]);
            if(prev_tracker[max_index] == max_index){
                break;
            }
            max_index = prev_tracker[max_index];
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<int> dummy;
        return tabulation(nums);
    }
};