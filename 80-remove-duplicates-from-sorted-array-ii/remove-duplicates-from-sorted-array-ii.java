class Solution {
    public int removeDuplicates(int[] nums) {
        int j = 0;
        int i = 0;

        int last_seen = -1;

        int last_seen_count = 0;

        while(j < nums.length){
            if (nums[j] != last_seen){
                last_seen = nums[j];
                last_seen_count = 1;
                nums[i] = nums[j];
                i += 1;
                j += 1;
            }
            else if (nums[j] == last_seen && last_seen_count < 2){
                
                last_seen_count += 1;
                nums[i] = nums[j];
                i += 1;
                j += 1;
            }else{
                j += 1;
            }
        }

        return i;
    }
}