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
    func swapNodes(_ head: ListNode?, _ k: Int) -> ListNode? {
        
        var slow : ListNode? = head;
        var fast : ListNode? = head;

        var left : ListNode? = head;
        var count: Int = 1;
        while count != k {
            left = left?.next;
            count += 1;
        }
        count = 0
        while count != k{
            fast = fast?.next;
            count += 1;
        }

        while fast != nil{
            fast = fast?.next;
            slow = slow?.next;
        }
        if let left = left, let right = slow{
            var temp: Int = left.val;
            left.val = right.val;
            right.val = temp;
        }
        return head
    }
}