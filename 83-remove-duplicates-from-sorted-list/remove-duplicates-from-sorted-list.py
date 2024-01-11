# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # #Approach1
        # ans = head
        # iterator = head
        # while(iterator != None):
        #     if iterator.val > ans.val:
        #         ans.next = iterator
        #         ans = iterator
        #     iterator = iterator.next
        
        # if (ans != None):
        #     ans.next = None
        # return head

        #Approach 2
        if not head:
            return head
        ans = head
        holder = head
        iterator = head
        while(iterator != None):
            if iterator.val > holder.val:
                holder.next = iterator
                holder = holder.next
            iterator = iterator.next
        
        holder.next = None

        return ans