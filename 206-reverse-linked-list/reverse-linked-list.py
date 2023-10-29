# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or  not head.next:
            return head
        previous = None
        return self.helper(head,previous)


    def helper(self,current,previous):
        if not current:
            return previous
        temp = current.next
        current.next = previous
        previous = current
        current = temp
        
        
        return self.helper(current,previous)