class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int currentMax = 0;
        int current = 0;
        int zeroesSeen = 0;
        int afterZero = 0;

        for(int j=0; j<nums.length; j++){
            if(nums[j]==0){
                zeroesSeen++;
            }
            if(zeroesSeen == 0){
                current++;
                if(current>currentMax){
                    currentMax=current;

                }
            }else if(zeroesSeen ==1){
                    current++;
                    afterZero++;
                    if(current>currentMax){
                        currentMax = current;
                    }
   
            }else if(zeroesSeen == 2){
                current = afterZero;
                afterZero = 1;
                zeroesSeen =1;
                
            }
        }
        return currentMax;
    }
}