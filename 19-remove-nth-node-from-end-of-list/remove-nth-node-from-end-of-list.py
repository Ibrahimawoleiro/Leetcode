# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Stall the back pointer for n number of times
        #If at this point fast is on None:
        #return back.next
        #Then move both back and front pointer
        #Keep a previous pointer that points to front of back
        
        back = head
        front = head
        previous = None

        while(n > 0):
            n -= 1
            front = front.next
        
        if front == None:
            return back.next
        while(front!= None):
            front = front.next
            previous = back
            back = back.next
        
        previous.next = previous.next.next

        return head