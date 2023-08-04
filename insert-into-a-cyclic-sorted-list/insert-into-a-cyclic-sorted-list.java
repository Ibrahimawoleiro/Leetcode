/*
// Definition for a Node.
class Node {
    public int val;
    public Node next;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _next) {
        val = _val;
        next = _next;
    }
};
*/

class Solution {
    public Node insert(Node head, int insertVal) {
        Node node = new Node(insertVal);
        if(head==null){
            node.next = node;
            return node;
        }
        Node current = head.next;
        Node previous = head;
        while(current != head){
            if(current==null){
                previous.next=node;
                node.next = previous;
                return head;
            }
            if((previous.val<=node.val && node.val<=current.val)||(previous.val<node.val && previous.val>current.val) || (previous.val>node.val && node.val<current.val && previous.val>current.val)){
                node.next = current;
                previous.next=node;
                return head;
            }
            previous=current;
            current=current.next;
        }
        System.out.println(current.val);
        previous.next=node;
        node.next=current;
        return head;
    }
}