# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        runner = head
        count = 0
        while(runner != None):
            count+=1
            runner = runner.next

        rotation = (k % count) + 1
        print(k,count,rotation)
        fast = head
        slow = head

        while rotation > 0:
            fast = fast.next
            rotation -= 1

        while(fast != None):
            fast = fast.next
            slow = slow.next
        
        if slow == None or slow.next == None:
            return head
        
        new_head = slow.next
        ans = new_head
        slow.next = None
        while(new_head.next != None):
            new_head = new_head.next
        new_head.next = head
        return ans

