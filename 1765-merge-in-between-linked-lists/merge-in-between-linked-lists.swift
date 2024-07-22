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
    func mergeInBetween(_ list1: ListNode?, _ a: Int, _ b: Int, _ list2: ListNode?) -> ListNode? {
        var head: ListNode? = list1;
        var count: Int = 0;
        var left: ListNode? = head;
        var right: ListNode? = nil;

        for index in stride(from: 0, to: b + 1, by: 1){
            head = head?.next;
            if index == a - 2{
                if let head = head{
                    left = head;
                }else{
                    return list1;
                }
            }
            if index == b-1{
                if let head = head{
                    right = head.next;
                }else{
                    return list1;
                }
            }
        }

        if a == b{
            right = left?.next?.next
        }
        
        var curr: ListNode? = list2;

        while curr?.next != nil{
            curr = curr?.next;
        }

        left?.next = list2!
        curr?.next = right

        return list1;
    }
}