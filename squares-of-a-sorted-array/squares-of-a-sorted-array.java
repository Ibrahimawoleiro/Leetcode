class Solution {
    public int[] sortedSquares(int[] nums) {
        int[] result = new int[nums.length];
        int resultEnd = nums.length-1;
        int end = nums.length-1;
        int start = 0;
        while(end>=start){
            if(nums[end] * nums[end] > nums[start] * nums[start]){
                result[resultEnd]=nums[end]*nums[end];
                end--;
                resultEnd--;
            }else{
                
                result[resultEnd]=nums[start] * nums[start];
                start ++;
                resultEnd--;
            }
        }
        return result;
    }
}