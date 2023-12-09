# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        ans = None
        real_ans = None
        while p1 != None or p2 != None:
            if(p1 and p2):
                if p1.val < p2.val:
                    if ans == None:
                        ans = p1
                        real_ans = ans
                        p1 = p1.next
                        continue
                    ans.next = p1
                    ans = p1
                    p1 = p1.next
                else:
                    if ans == None:
                        ans = p2
                        real_ans = ans
                        p2 = p2.next
                        continue
                    ans.next = p2
                    ans = p2
                    p2 = p2.next
            elif(p2 == None):
                if ans == None:
                    return p1
                ans.next = p1
                return real_ans
            elif p1 == None:
                if ans == None:
                    return p2
                ans.next = p2
                return real_ans
        
        return real_ans