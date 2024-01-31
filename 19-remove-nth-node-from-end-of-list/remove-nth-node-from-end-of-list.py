# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Approach 1
        # if head.next == None and n>0:
        #     return None
        # result = ListNode()
        # result.next = head
        # fast = result
        # slow = result

        # while fast != None:
        #     if n+1 > 0:
        #         fast = fast.next
        #         n-=1
        #     else:
        #         fast = fast.next
        #         slow = slow.next

        # if slow.next!=None:
        #     slow.next = slow.next.next
        
        # return result.next

        #Approach 2
        delayed = ListNode()
        ans = delayed
        delayed.next = head
        runner = head

        while(runner):
            if n > 0:
                runner = runner.next
                n-=1
                continue
            runner = runner.next
            delayed = delayed.next

        delayed.next = delayed.next.next

        return ans.next
            

