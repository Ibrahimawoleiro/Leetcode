class Solution {
    public int maxProfit(int[] prices) {

        // //1
        // int maximum = 0;
        // for(int i = 0; i< prices.length; i++){
        //     for(int j = i+1; j<prices.length; j++){
        //         if (prices[j] - prices[i] > maximum){
        //             maximum = prices[j] - prices[i];
        //         }
        //     }
        // }
        // return maximum;

        //2
        int i = 0;
        int j = 0;
        int maximum = 0;
        while(j < prices.length){
            if(prices[i] < prices[j]){
                if(prices[j] - prices[i] > maximum){
                    maximum = prices[j] - prices[i];
                }
            }else{
                i = j;
            }
            j++;
        }
        return maximum;
    }
}