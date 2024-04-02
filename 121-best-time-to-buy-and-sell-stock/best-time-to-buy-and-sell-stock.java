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

        // //2
        // int i = 0;
        // int j = 0;
        // int maximum = 0;
        // while(j < prices.length){
        //     if(prices[i] < prices[j]){
        //         if(prices[j] - prices[i] > maximum){
        //             maximum = prices[j] - prices[i];
        //         }
        //     }else{
        //         i = j;
        //     }
        //     j++;
        // }
        // return maximum;

        //3
        int i = 0;
        int[] diff = new int[prices.length - 1];
        while(i+1<prices.length){
            diff[i] = prices[i+1] - prices[i];
            i+=1;
        }
        int maximum = 0;
        int curr_sum = 0;
        int runner = 0;
        while(runner < diff.length){
            if (diff[runner] + curr_sum > diff[runner]){
                curr_sum += diff[runner];
            }else{
                curr_sum = diff[runner];
            }
            if(curr_sum > maximum){
                maximum = curr_sum;
            }
            runner+=1;
        }
        return maximum;
    }
}