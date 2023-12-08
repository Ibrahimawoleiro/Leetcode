# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # #Approach1
        # arr = []
        # while head != None:
        #     arr.append(head.val)
        #     head = head.next
        
        # front_pointer = 0
        # back_pointer = len(arr) - 1
        # while(front_pointer <= back_pointer):
        #     if(arr[front_pointer] != arr[back_pointer]):
        #         return False
        #     front_pointer += 1
        #     back_pointer -= 1
        
        # return True

        # #Approach2
        # slow = head
        # fast = head
        # arr=[]
        # while(fast != None and fast.next != None):
        #     arr.append(slow.val)
        #     slow = slow.next
        #     fast = fast.next.next
        # if fast == None:
        #     while(slow != None):
        #         if(slow.val != arr.pop()):
        #             return False
        #         slow = slow.next
        # elif fast.next == None:
        #     slow = slow.next
        #     while(slow != None):
        #         if(slow.val != arr.pop()):
        #             return False
        #         slow = slow.next
        # return True

        #Approach3
        if(head.next == None):
            return True

        slow = head
        fast = head
        previous = None
        while(fast != None and fast.next != None):
            previous = slow
            slow = slow.next
            fast = fast.next.next
        
        if fast == None:
            previous.next = None
            previous = None
            curr = slow
            next = None
            while(curr != None):
                next = curr.next
                curr.next = previous
                previous = curr
                curr = next

            checker = head
            while(previous != None):
                if previous.val != checker.val:
                    return False
                previous = previous.next
                checker = checker.next
        
        elif fast.next == None:
            slow = slow.next
            previous.next = None
            previous = None
            curr = slow
            next = None
            while(curr != None):
                next = curr.next
                curr.next = previous
                previous = curr
                curr = next

            checker = head
            while(previous != None):
                if previous.val != checker.val:
                    return False
                previous = previous.next
                checker = checker.next
        
        return True

            
            
