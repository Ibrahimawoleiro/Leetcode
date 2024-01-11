# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Approach1
        curr = head
        stack = []
        while(curr != None):
            stack.append(curr.val)
            curr = curr.next
        ans = ListNode()
        result = ans
        while(stack):
            ans.next = ListNode(val = stack.pop(), next = None)
            ans = ans.next
        
        return result.next