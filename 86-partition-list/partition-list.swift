/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init() { self.val = 0; self.next = nil; }
 *     public init(_ val: Int) { self.val = val; self.next = nil; }
 *     public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
 * }
 */
class Solution {
    func partition(_ head: ListNode?, _ x: Int) -> ListNode? {
        var lower: ListNode? = ListNode();
        var greater: ListNode? = ListNode();

        var lower_runner: ListNode? = lower;
        var greater_runner: ListNode? = greater;

        var itr: ListNode? = head;

        while itr != nil{
            if itr!.val < x {
                lower_runner?.next = itr;
                itr = itr!.next
                lower_runner = lower_runner?.next;
                lower_runner!.next = nil
            }else{
                greater_runner?.next = itr;
                itr = itr!.next
                greater_runner = greater_runner?.next;
                greater_runner!.next = nil
            }
        }

        lower_runner!.next = greater!.next
        return lower!.next;

    }
}