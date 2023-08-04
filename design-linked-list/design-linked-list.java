class MyLinkedList {
    
    Node head=null;
    Node tail=null;
    int count=0;
    
    class Node{
        int data;
        Node next;
        Node previous;
        public Node(int data, Node next, Node previous){
            this.data = data;
            this.next = next;
            this.previous = previous;
        }
    }

    public MyLinkedList() {
        head = new Node(Integer.MIN_VALUE,null,null);
        tail = new Node(Integer.MIN_VALUE,null,null);  
    }
    
    public int get(int index) {
        if(index<0 || index > count-1){
            return -1;
        }
        Node holder = head;
        for(int i=0; i<=index; i++){
            holder = holder.next;
        }
        return holder.data;
    }
    
    public void addAtHead(int val) {
        Node input= new Node(val,null,null);
        if(count>0){
            input.next=head.next;
            input.previous =head;
            head.next.previous=input;
            head.next = input;
            count++;
            return;
        }
        head.next=input;
        input.previous = head;
        input.next = tail;
        tail.previous = input;
        count++;
    }
    
    public void addAtTail(int val) {
        Node input = new Node(val,null,null);
        if(count>0){
            input.next =tail;
            input.previous = tail.previous;
            tail.previous=tail.previous.next = input;
            count++;
            return;
        }
        head.next=input;
        input.previous = head;
        input.next = tail;
        tail.previous = input;
        count++;
    }
    
    public void addAtIndex(int index, int val) {
        
        if(index<0 || index > count){
            return;
        }
        Node temp = new Node(val,null,null);
        if(index==0 && count>0){
            temp.next=head.next;
            temp.previous =head;
            head.next.previous=temp;
            head.next = temp;
            count++;
            return;
        }else if(index==0 && count==0){
            head.next=temp;
            temp.previous = head;
            temp.next = tail;
            tail.previous = temp;
            count++;
            return;
        }
        Node holder = head;
        for(int i=0; i<=index-1; i++){
            holder = holder.next;
        }
        temp.next = holder.next;
        temp.previous=holder;
        holder.next.previous= temp;
        holder.next = temp;
        count++;
    }
    
    public void deleteAtIndex(int index) {
        if(index<0 || index > count-1 || count==0){
            return;
        }
        Node holder = head;
        for(int i=0; i<=index-1; i++){
            holder = holder.next;
        }
        Node temp =holder.next;
        holder.next = temp.next;
        temp.next.previous = holder;
        count--;
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */