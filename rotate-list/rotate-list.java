/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
     public ListNode rotateRight(ListNode head, int k) {
        ListNode prev =null;
        ListNode temp= head;
        int count=1;
        if(head==null || head.next==null|| k==0){
            return head;
        }
        while(head.next!=null){
            count++;
            head=head.next;
        }
         if(count<k){
             k=k%count;
         }
         head=temp;
        for(int i=0;i<k;i++){
            while(head.next!=null){
                prev=head;
                head=head.next;
            }
            head.next=temp;
            temp=head;
            prev.next=null;
        }
        return temp;
    }
}