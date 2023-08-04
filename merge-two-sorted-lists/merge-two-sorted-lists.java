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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if(list1==null){
            return list2;
        }
        if(list2==null){
            return list1;
        }
        ListNode target = new ListNode(0);
        ListNode ans = target;
        while(list1!=null || list2!=null){
            if(list1!=null && list2!=null){
                if(list1.val<list2.val){
                    target.next=list1;
                    target = target.next;
                    list1=list1.next;
                }else{
                    target.next=list2;
                    target = target.next;
                    list2=list2.next;
                }
            }else if(list1==null){
                target.next=list2;
                return ans.next;
            }else if(list2==null){
                target.next=list1;
                return ans.next;
            }
        }
        return null;
        
    }
}