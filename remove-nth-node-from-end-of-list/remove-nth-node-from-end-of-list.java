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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if(head==null){
            return null;
        }
        ListNode first=head;
        ListNode second=head;
        ListNode remover=null;
        int delay = n;
        while(first!=null){
            if(delay<=0){
                remover=second;
                second = second.next;
            }
            first=first.next;
            delay--;
        }
        if(remover==null){
            return second.next;
        }
        remover.next = second.next;
        second.next = null;
        return head;
    }
}