class MyQueue {
    int peek = -1;
    Stack<Integer> stackA = new Stack<>();
    Stack<Integer> stackB = new Stack<>();
    public MyQueue() {
        
    }
    
    public void push(int x) {
        if(this.peek == -1){
            this.peek = x;
        }
        this.stackA.push(x);
    }
    
    public int pop() {
        while(!this.stackA.isEmpty()){
            this.stackB.push(this.stackA.pop());
        }
        int result = this.stackB.pop();
        if (!stackB.isEmpty()){
            this.peek = stackB.peek();
        }else{
            this.peek = -1;
        }
        while(!this.stackB.isEmpty()){
            this.stackA.push(this.stackB.pop());
        }
        return result;
    }
    
    public int peek() {
        return this.peek;
    }
    
    public boolean empty() {
        return stackA.isEmpty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */