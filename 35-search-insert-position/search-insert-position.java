class Solution {
    public int searchInsert(int[] nums, int target) {
        // //1
        // if (target > nums[nums.length - 1]){
        //     return nums.length;
        // }else if(target < nums[0]){
        //     return 0;
        // }
        // for(int i = 0; i < nums.length; i++){
        //     if (nums[i] >= target){
        //         return i;
        //     }
        // }
        // return -1;

        //2
        int high = nums.length - 1;
        int low = 0;
        while(low <= high){
           int mid = (low + high) / 2;
           if (nums[mid] >= target){
            high = mid - 1;
           }else{
            low = mid + 1;
           }
        }
        return high + 1;
    }
}