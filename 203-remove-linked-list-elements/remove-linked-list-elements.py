# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None or (head.next == None and head.val != val):
            return head
        ans = None
        previous = None
        current = head

        while(current != None):
            if current.val != val and ans == None:
                ans = current 
                previous = current 
            elif current.val != val:
                previous.next = current
                previous = current 
            current = current.next
        if previous != None:
            previous.next = None
        return ans
            