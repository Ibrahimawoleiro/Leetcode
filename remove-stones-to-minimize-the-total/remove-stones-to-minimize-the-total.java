class Solution {
    public int minStoneSum(int[] piles, int k) {
        PriorityQueue<Integer> heap = new PriorityQueue<>(Comparator.reverseOrder());
        for(int val : piles){
            heap.add(val);
        }
        int number = 0;
        for(int i = 0; i<k; i++){
            number = heap.remove();
            number = (int)( number - Math.floor(number/2));
            heap.add(number);
        }
        int total = 0;
        
        while(!heap.isEmpty()){
            int l = heap.remove();
            total+=l;
        }
        return total;
    }
}