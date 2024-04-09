class Solution {
    public int findShortestSubArray(int[] nums) {
        HashMap<Integer, Integer[]> map = new HashMap<>();
        for(int index = 0; index < nums.length; index++){
            if(!map.containsKey(nums[index])){
                map.put(nums[index], new Integer[3]);
                map.get(nums[index])[0] = 1;
                map.get(nums[index])[1] = index;
                map.get(nums[index])[2] = index;
            }else{
                map.get(nums[index])[0]++;
                map.get(nums[index])[2] = index;
            }
        }
        int smallest = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        for (Integer key : map.keySet()) {
            Integer[] curr = map.get(key);
            if(curr[0] > max){
                smallest = (curr[2] - curr[1]) + 1;
                max = curr[0];
            }else if (curr[0] == max && (curr[2] - curr[1]) + 1 < smallest){
                smallest = (curr[2] - curr[1]) + 1;
                max = curr[0];
            }
        }
        return smallest;
    }
}