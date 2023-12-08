# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # #Approach1
        # while(head != None):
        #     if head == None:
        #         return False
        #     if(hasattr(head, 'seen')):
        #         return True
        #     else:
        #         head.seen = True
        #     head = head.next

        #Approach2
        fast = head
        slow = head

        while(fast != None and fast.next!= None):
          slow = slow.next
          fast = fast.next.next
          if slow == fast:
            return True
        return False