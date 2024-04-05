class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int curr = 0;
        int max = 0;
        int i = 0;
        while(i < nums.length){
            if(nums[i] == 0){
                curr = 0;
                i+=1;
                continue;
            }
            if(nums[i] == 1){
                curr += 1;
                if (curr > max){
                    max = curr;
                }
                i += 1;
            }
        }
        return max;
    }
}