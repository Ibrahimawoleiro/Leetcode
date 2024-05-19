# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head.next
        if not head.next.next:
            head.next = None
            return head
        if not head.next.next.next:
            head.next = head.next.next
            return head
        count = 0

        temp = head

        while temp:
            count += 1
            temp = temp.next
        
        steps = (ceil(count / 2 ) + 1)

        temp = head
        while steps > 0:
            temp = temp.next
            steps -= 1

        if not temp:
            return head

        helper = head

        while(temp):
            temp = temp.next
            helper = helper.next

        helper.next = helper.next.next

        return head
