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
    public ListNode removeElements(ListNode head, int val) {
        ListNode current = head;
        ListNode temp = null;
        while(current!=null){
            if(current.val==val){
                if(current==head){
                    head=head.next;
                    current=head;
                    continue;
                }else{
                    temp.next=current.next;
                    current=temp.next;
                    continue;
                }
            }
            temp=current;
            current=current.next;
        }
        return head;
    }
}