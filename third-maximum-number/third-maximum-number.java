class Solution {
    public int thirdMax(int[] nums) {
        Arrays.sort(nums);
        int thirdmax=0;
        int changes = 2;
        int currentHighest=nums[nums.length-1];
        for(int i=nums.length-1; i>-1; i--){
            if(nums[i]!=currentHighest && changes>0){
                thirdmax=nums[i];
                currentHighest=nums[i];
                changes--;
            }
            if(changes<=0){
                return thirdmax;
            }
        }
        return nums[nums.length-1];
    }
}