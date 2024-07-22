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
    func removeNodes(_ head: ListNode?) -> ListNode? {
        var stack: [Int] = [Int]();

        var curr: ListNode? = head;

        while curr != nil{
            while stack.count > 0{
                guard let last = stack.last else {break}
                var curr_value: Int? = curr?.val;
                if last < curr_value!{
                    stack.popLast();
                }else{
                    break;
                }
            }

            if let curr = curr{
                let num = curr.val;
                    stack.append(num);
            }

            curr = curr?.next;
        }

        print(stack)
        var ans: ListNode? = ListNode();
        var iterator: ListNode? = ans;
        for num in stack{
            print(num)
            var curr: ListNode? = ListNode(num);
            if let itr = iterator{
                itr.next = curr;
                iterator = itr;
                iterator = iterator?.next;
            }
        }
        return ans!.next;


    }
}