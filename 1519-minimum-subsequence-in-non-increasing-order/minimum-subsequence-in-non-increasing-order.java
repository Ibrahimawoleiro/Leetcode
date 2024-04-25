class Solution {
    public List<Integer> minSubsequence(int[] nums) {
        int nums_sum = 0;
        for(int v: nums){
            nums_sum += v;
        }
        ArrayList<Integer> ans = new ArrayList<>();
        int ans_sum = 0;
        Arrays.sort(nums);
        int i = nums.length - 1;
        while(ans_sum <= nums_sum){
            int curr = nums[i];
            nums_sum -= curr;
            ans_sum += curr;
            ans.add(curr);
            i -=1;
        }

        return ans;
    }
}