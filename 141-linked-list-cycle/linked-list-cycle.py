# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # #Approach1
        # fast = head
        # slow = head

        # while(fast != None and fast.next != None):
        #     slow = slow.next
        #     fast = fast.next.next
        #     if fast == slow:
        #         return True
        # return False

        #Approach 2
        while(head != None):
            head.seen = True
            head = head.next
            if hasattr(head,'seen'):
                return True

        return False