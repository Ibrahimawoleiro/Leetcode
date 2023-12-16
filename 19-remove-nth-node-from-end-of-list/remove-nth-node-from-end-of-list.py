# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head.next == None and n>0:
            return None
        result = ListNode()
        result.next = head
        fast = result
        slow = result

        while fast != None:
            if n+1 > 0:
                fast = fast.next
                n-=1
            else:
                fast = fast.next
                slow = slow.next

        if slow.next!=None:
            slow.next = slow.next.next
        
        return result.next