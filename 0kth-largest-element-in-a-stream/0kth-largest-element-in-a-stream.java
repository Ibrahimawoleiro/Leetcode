class KthLargest {
    
    /*
    PriorityQueue<Integer> heap = new PriorityQueue<>();

// Add to heap
heap.add(1);
heap.add(2);
heap.add(3);

// Check minimum element
heap.peek(); // 1

// Pop minimum element
heap.remove(); // 1

// Get size
heap.size(); // 2

// Bonus: if you want a max heap instead, you can pass
// Comparator.reverseOrder() to the constructor:
PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());
    */
    
    PriorityQueue<Integer> heap = new PriorityQueue<>();
    int k;
    
    public KthLargest(int k, int[] nums) {
        this.k = k;
        Arrays.sort(nums);
        for(int val : nums){
            heap.add(val);
        }
        if(nums.length > k){
            while(heap.size()>k){
                heap.remove();
            }
        }
    }
    
    public int add(int val) {
        int number = 0;
        if( heap.size() == k) 
        {
            
            heap.add(val);
            heap.remove();
            return heap.peek();
        }else
        {
            heap.add(val);
            
            return heap.peek();
        }
    
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */