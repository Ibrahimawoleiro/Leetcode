class Solution {
    public int minOperations(int[] nums) {
        int i = 0;
        int count = 0;
        while(i + 1 < nums.length){
            if(nums[i]< nums[i+1]){
                i+=1;
                continue;
            }
            int curr_count = (nums[i] - nums[i+1]) + 1;
            count += curr_count;
            nums[i+1] = curr_count + nums[i+1]; 
            i+=1;
        }
        return count;
    }
}