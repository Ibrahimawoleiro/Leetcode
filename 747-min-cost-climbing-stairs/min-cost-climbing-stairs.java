class Solution {
    public int minCostClimbingStairs(int[] cost) {
    //     //1
    //     return Math.min( Math.min(cost[0]+r(1,cost),cost[0]+r(2,cost)), Math.min(cost[1]+r(2,cost),cost[1]+r(3,cost)));
    // }

    // public int r(int index, int[] cost){
    //         if(index >= cost.length){
    //             return 0;
    //         }else if(index == cost.length - 1){
    //             return cost[index];
    //         }
    //         return Math.min(cost[index] + r(index + 1, cost), cost[index] + r(index + 2, cost));
    // }


        //2
        HashMap<Integer,Integer> store = new HashMap<>();
        return Math.min( Math.min(cost[0]+r(1,cost, store),cost[0]+r(2,cost, store)), Math.min(cost[1]+r(2,cost,store),cost[1]+r(3,cost,store)));
    }

    public int r(int index, int[] cost, HashMap<Integer,Integer> store){
            if(index >= cost.length){
                return 0;
            }else if(index == cost.length - 1){
                return cost[index];
            }
            if(store.containsKey(index)){
                return store.get(index);
            }
            int curr = Math.min(cost[index] + r(index + 1, cost, store), cost[index] + r(index + 2, cost, store));
            store.put(index, curr);
            return curr;
    }


    
}