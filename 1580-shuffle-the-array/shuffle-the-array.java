class Solution {
    public int[] shuffle(int[] nums, int n) {
        int i = 0;
        System.out.println(n);
        int j = n;
        int[] result = new int[n*2];
        int k = 0;
        while(k < n*2){

                result[k] = nums[i];
                i++;
                k++;


                result[k] = nums[j];
                j++;
                k++;
        }
        return result;
    }
}