# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rem = 0
        ans = ListNode()
        result = ans
        while(l1 or l2):
            if l1 and l2:
                curr = l1.val + l2.val + rem
                if curr > 9:
                    ans.next = ListNode(curr % 10)
                    rem = 1
                else:
                    ans.next = ListNode(curr)
                    rem = 0
                ans = ans.next
                l1 = l1.next
                l2 = l2.next
            elif l1:
                curr = l1.val + rem
                if curr > 9:
                    ans.next = ListNode(curr % 10)
                    rem = 1
                else:
                    ans.next = ListNode(curr)
                    rem = 0
                l1 = l1.next
                ans = ans.next
            else:
                curr = l2.val + rem
                if curr > 9:
                    ans.next = ListNode(curr % 10)
                    rem = 1
                else:
                    ans.next = ListNode(curr)
                    rem = 0
                l2 = l2.next
                ans = ans.next
        
        if rem == 1:
            ans.next = ListNode(1)
        
        return result.next


        