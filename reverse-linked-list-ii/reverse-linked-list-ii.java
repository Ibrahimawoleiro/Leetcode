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
    public ListNode reverseBetween(ListNode head, int left, int right) {
        ListNode left_holder = null;
        ListNode right_holder = null;
        int position_count = 1;
        if(left == right){
            return head;
        }
        
        if(left == 1){
            left_holder = head;
            ListNode current = head;
            ListNode previous = null;
            ListNode next_node = current.next;
            while(position_count <= right){
                if(position_count == right){
                    head = current;
                }
                current.next = previous;
                previous = current;
                current = next_node;
                if(next_node != null){
                    next_node = current.next;
                }
                position_count += 1;
                
            }
            left_holder.next = current;
        }
        if(left > 1){
            ListNode current = head;
            ListNode previous = null;
            ListNode next_node = null;
            position_count = 1;
            ListNode left_node = null;
            
            while(position_count <= right){
                if(position_count == left -1){
                    left_holder = current;
                }
                if(position_count >= left){
                    if(position_count == right){
                        current.next = previous;
                        previous = current;
                        current = next_node;
                        break;
                    }
                    if(position_count == left){
                        left_node = current;
                        next_node = current.next;
                    }
                    current.next = previous;
                    previous = current;
                    current = next_node;
                    next_node = current.next;
                    position_count+=1;
                    continue;
                }
                current = current.next;
                position_count+=1;
            }
            left_holder.next = previous;
            left_node.next = current;
        }
        return head;
        /*
        if left > 1:
            current = head
            previous = None
            next_node = None
            position_count = 1
            left_node = None
            
            while(position_count <= right):
                if position_count == left - 1:
                    left_holder = current
                if(position_count >= left):
                    if(position_count == right):
                        current.next = previous
                        previous = current
                        current = next_node
                        break
                    if position_count == left:
                        left_node = current
                        next_node = current.next
                    current.next = previous
                    previous = current
                    current = next_node
                    next_node = current.next
                    position_count+=1
                    continue
                current = current.next
                position_count+=1
            left_holder.next = previous
            left_node.next = current
        return head
        */
    }
}