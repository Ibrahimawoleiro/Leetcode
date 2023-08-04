class Solution {
    public int removeDuplicates(int[] nums) {
        int i = -1;
        int j = 0;
        int highest = Integer.MIN_VALUE;
        while(j<nums.length){
            if(nums[j]>highest){
                highest = nums[j];
                int temp = nums[i+1];
                nums[i+1]=nums[j];
                nums[j]=temp;
                i++;
            }
            j++;
        }
        return i+1;
    }
}