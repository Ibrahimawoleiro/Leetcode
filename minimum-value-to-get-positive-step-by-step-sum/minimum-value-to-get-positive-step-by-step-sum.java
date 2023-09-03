class Solution {
    public int minStartValue(int[] nums) {
        //add starter=0 to the first index
        //add the first index to the second and so on....
        //keep track of this addition 
        //if there is a case where the sum < 1
        //break out of the current addition and increase starter by one and repeat the steps above
        
        int starter = 1;
        while(true){
            int sum = 0;
            sum+=starter;
            for(int i = 0; i<nums.length; i++){
                sum+=nums[i];
                if(sum<1){
                    break;
                }
            }
            if(sum>=1){
                return starter;
            }
            starter++;
        }
    }
}