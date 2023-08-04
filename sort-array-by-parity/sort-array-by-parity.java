class Solution {
    public int[] sortArrayByParity(int[] nums) {
        int i =0;
        for(int j=0; j<nums.length; j++){
            if(nums[i]%2==1 && nums[j]%2==1){
                continue;
            }else if(nums[i]%2==1 && nums[j]%2==0){
                int temp = nums[i];
                nums[i]=nums[j];
                nums[j]=temp;
                i++;
            }else{
                 i++;
            }
        }
        return nums;
    }
}