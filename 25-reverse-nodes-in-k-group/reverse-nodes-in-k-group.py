# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(node):
            if not node:
                return
            prev = None
            curr = node
            while(node):
                next_ = node.next
                node.next = prev
                prev = node
                node = next_
            
            return prev


        
        def k_reverse(node):
            if not node:
                return None
            
            back_up = node
            r = k - 1
            while(r != 0 and node):
                node = node.next
                r-=1
            if not node:
                return back_up
            
            next_back_up = node.next
            node.next = None

            head_of_reversed = reverse(back_up)
            back_up.next = k_reverse(next_back_up)
            return head_of_reversed
        return k_reverse(head)

