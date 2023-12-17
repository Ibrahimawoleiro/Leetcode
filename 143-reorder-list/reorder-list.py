# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        count = 0
        previous = None
        slow = head 
        fast = head
        while(fast != None and fast.next!= None):
            fast = fast.next.next
            if count != 0:
                previous = slow
            slow = slow.next
            count+=1
        
        if (count == 1 or count == 0) and not slow.next:
            return 
        if not previous:
            previous = head
        previous.next = None
        curr = slow
        prev = None
        next_holder = None
        while(curr):
            next_holder = curr.next
            curr.next = prev
            prev = curr
            curr = next_holder

        print(slow)
        #print(prev, slow)
        slow = head
        temp1 = None
        temp2 = None
        
        while(prev and slow):
            temp1 = slow.next 
            if prev:
                slow.next = prev
            temp2 = prev.next
            if temp1:
                prev.next = temp1
            slow = temp1
            prev = temp2
        
