class MyStack {
    Queue<Integer> queueA = new LinkedList<>();
    Queue<Integer> queueB = new LinkedList<>();
    int peek = -1;
    public MyStack() {
        
    }
    
    public void push(int x) {
        this.peek = x;
        this.queueA.offer(x);
    }
    
    public int pop() {
        int result = -1;
        while(this.queueA.size() > 1){
            queueB.offer(queueA.poll());

        }
        result = queueA.poll();
        
        while(!this.queueB.isEmpty()){
            if(queueB.size() == 1){
                this.peek = queueB.peek();
            }
            queueA.offer(queueB.poll());

        }
        return result;
    }
    
    public int top() {
        return this.peek;
    }
    
    public boolean empty() {
        return queueA.isEmpty();
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */