class Solution {
    public int[] sortArrayByParity(int[] nums) {
        int i = 0;
        int j = 0;
        while(j< nums.length && i < nums.length){
            if(i==j){
                j++;
            }else if(nums[i] % 2 == 0){
                i+=1;
            }else if(nums[j] % 2 == 1 && nums[i] % 2 ==1){
                j++;
            }else{
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
            }
        } 
        return nums;
    }
}