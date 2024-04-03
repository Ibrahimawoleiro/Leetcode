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


    //     //2
    //     HashMap<Integer,Integer> store = new HashMap<>();
    //     return Math.min( Math.min(cost[0]+r(1,cost, store),cost[0]+r(2,cost, store)), Math.min(cost[1]+r(2,cost,store),cost[1]+r(3,cost,store)));
    // }

    // public int r(int index, int[] cost, HashMap<Integer,Integer> store){
    //         if(index >= cost.length){
    //             return 0;
    //         }else if(index == cost.length - 1){
    //             return cost[index];
    //         }
    //         if(store.containsKey(index)){
    //             return store.get(index);
    //         }
    //         int curr = Math.min(cost[index] + r(index + 1, cost, store), cost[index] + r(index + 2, cost, store));
    //         store.put(index, curr);
    //         return curr;
    // }

        int i = cost.length - 1;
        while(i >= 0){
            if(i == cost.length - 1 || i+1 >= cost.length || i + 2 >= cost.length){
                i--;
                continue;
            }
            cost[i] = Math.min(cost[i] + cost[i + 1], cost[i]+ cost[i+2]);
            i--;
        }

        return Math.min(cost[0], cost[1]);
    }
}