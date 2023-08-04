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
    public boolean isPalindrome(ListNode head) {
        int count = 0;
        ListNode run1 = head;
        ListNode stopper = null;
        ListNode holder=null;
        while(run1!=null){
            count++;
            run1=run1.next;
        }
        run1=head;
        if(count==1){
            return true;
        }
        if(count%2==0){
            count/=2;
            while(count>0){
                run1=run1.next;
                count--;
            }
            stopper = run1;
            holder=reverseLinkedList(run1);
            run1=head;
            while(run1!=stopper){
                if(run1.val!=holder.val){
                    return false;
                }
                holder=holder.next;
                run1=run1.next;
            }
        }else{
            count/=2;
            while(count>-1){
                run1=run1.next;
                count--;
            }
            stopper = run1;
            holder = reverseLinkedList(run1);
            run1=head;
            while(holder!=null){
                if(holder.val!=run1.val){
                    return false;
                }
            holder=holder.next;
            run1=run1.next;
            }
            
        }
        return true;
    }
    public static ListNode reverseLinkedList(ListNode node){
        ListNode temp = node.next;
        ListNode previous = null;
        while(node!=null){
            temp=node.next;
            node.next=previous;
            previous=node;
            node=temp;
        }
        return previous;
    }
}