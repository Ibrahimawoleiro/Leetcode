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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int remainder = 0;
        ListNode backup = l2;
        ListNode previous = null;
        while(l1!=null || l2!=null){
            if(l1!=null && l2!=null){
                int sum = l1.val +l2.val+remainder;
                l2.val = sum%10;
                if(sum>=10){
                    remainder = 1;
                }else{
                    remainder = 0;
                }
                previous=l2;
                l1=l1.next;
                l2=l2.next;
            }else if(l1==null){
                if(remainder>0){
                    int sum = l2.val+remainder;
                    l2.val = sum % 10;
                    previous = l2;
                    l2 = l2.next;
                    if(sum>=10){
                        remainder = 1;
                    }else{
                        remainder = 0;
                        return backup;
                    }
                }else{
                    previous.next = l2;
                    return backup; 
                }
            }else if(l2==null){
                if(remainder>0){
                    int sum = l1.val+remainder;
                    l1.val = sum % 10;
                    previous.next = l1;
                    previous=l1;
                    l1 = l1.next;
                    if(sum>=10){
                        remainder = 1;
                    }else{
                        remainder = 0;
                        
                    }
                }else{
                   previous.next = l1;
                    return backup; 
                }
            }
        }
        if(remainder>0){
            ListNode ans = new ListNode(1);
            previous.next=ans; 
        }
        return backup;
        
    }
}