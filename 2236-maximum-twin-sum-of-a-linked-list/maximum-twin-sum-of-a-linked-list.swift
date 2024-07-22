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
    func pairSum(_ head: ListNode?) -> Int {
        var reverse: (ListNode?) -> ListNode? = { (curr: ListNode?) in
            guard let curr = curr else {return nil};
            var current : ListNode? = curr;
            var prev: ListNode? = nil;
            var next: ListNode? = nil;
            while current != nil{
                next = current?.next;
                current?.next = prev;
                prev = current;
                current = next;
            }
            return prev;
        }

        var fast: ListNode? = head;
        var slow: ListNode? = head;
        var prev: ListNode? = head;
        while fast != nil{
            prev = slow;
            fast = fast?.next?.next;
            slow = slow?.next;
        }
        if let prev = prev{
            prev.next = nil;
        }

        slow = reverse(slow);

        

        var maximum : Int = 0;
        fast = head;

        while fast != nil{
            
            guard let slow_node = slow else {break}
            guard let fast_node = fast else {break}
            maximum = max(maximum, (slow_node.val + fast_node.val))
            fast = fast?.next;
            slow = slow?.next;
        }

        return maximum;
    }
}