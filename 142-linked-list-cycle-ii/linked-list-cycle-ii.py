# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = head
        fast = head

        while(fast is not None and fast.next is not None):
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        
        if fast is not None and fast.next is not None:
            slow = head
            while(slow != fast):
                slow = slow.next
                fast = fast.next
                print(fast.val, slow.val)
            return fast
        
        return None