class Solution {
    public int removeElement(int[] nums, int val) {
        int i=0;
        for(int j=0; j<nums.length; j++){
            if(nums[i]==val && nums[j]!=val){
                int temp = nums[i];
                nums[i]=nums[j];
                nums[j]=temp;
                i++;
            }else if(nums[i]!=val){
                i++;
            }
        }
        return i;
    }
}