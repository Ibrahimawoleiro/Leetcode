# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        arr = []
        
        while( head != None):
            arr.append(head.val)
            head = head.next
        
        arr.sort()

        result = ListNode()
        ans = result
        for val in arr:
            result.next = ListNode(val)
            result = result.next

        return ans.next