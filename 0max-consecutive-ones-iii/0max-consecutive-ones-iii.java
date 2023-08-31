class Solution {
    
    public int longestOnes(int[] nums, int k) {
        int left = 0;
        int right = 0;
        int zero_count = 0;
        int current_max_window = 0;
        int highest_max_window = 0;
        
        while(right < nums.length){
            if (nums[right] == 1 || (nums[right] == 0 && zero_count<k)){
                if(nums[right]==0){
                    zero_count+=1;
                }
                current_max_window +=1;

                right+=1;
            }else{
                if (nums[left] == 0){
                    zero_count-=1;
                }
                left+=1;
                current_max_window-=1;
            }
            if(current_max_window>highest_max_window){
                highest_max_window = current_max_window;
            }
        }
        return highest_max_window;
    }
}