class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<Integer>(Collections.reverseOrder());
        for(int v: stones){
            maxHeap.add(v);
        }
        
        while(maxHeap.size() > 0){
            int curr = maxHeap.poll();
            if(maxHeap.isEmpty()){
                return curr;
            }
            int next = maxHeap.poll();
            
            if(curr == next){
                continue;
            }else{
                maxHeap.add(Math.abs(curr - next));
            }
        }

        return 0;
    }
}