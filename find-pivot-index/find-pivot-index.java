class Solution {
    public int pivotIndex(int[] nums) {
        int sum=0;
        int left=0;
        for(int x: nums){sum+=x;}
        for(int i=0; i<nums.length;i++){

            if(sum-(left+nums[i])==left){
                return i;
            }
            left+=nums[i];
        }
        return -1;
    }
}