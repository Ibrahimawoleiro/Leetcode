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
    func getDecimalValue(_ head: ListNode?) -> Int {
        var runner: ListNode? = head;
        var result: [Int] = [Int]()
        var ans = 0
        while runner != nil{
            if let val = runner?.val{
                 result.append(val)
            }
            runner = runner?.next
        }
        var count: Int = result.count - 1;
        for val in result{
            ans += val * Int(pow(2, Double(count)))
            count-=1
        }
        return ans
    }
}