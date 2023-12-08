# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #Approach1
        arr = []
        while head != None:
            arr.append(head.val)
            head = head.next
        
        front_pointer = 0
        back_pointer = len(arr) - 1
        while(front_pointer <= back_pointer):
            if(arr[front_pointer] != arr[back_pointer]):
                return False
            front_pointer += 1
            back_pointer -= 1
        
        return True
