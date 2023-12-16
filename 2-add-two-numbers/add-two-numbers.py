# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        extra = 0
        result = ListNode()
        iterator = result
        while(l1 or l2):
            if l1 and l2:
                if extra:
                    addition = extra + l1.val + l2.val
                    if addition>=10:
                        iterator.next = ListNode(addition % 10)
                        iterator = iterator.next
                        checker = int(floor(addition / 10))
                        if checker:
                            extra = checker
                    else:
                        iterator.next = ListNode(addition % 10)
                        iterator = iterator.next
                        print(int(floor(addition / 10)))
                        checker = int(floor(addition / 10))
                        if checker:
                            extra = checker
                        else:
                            extra = 0
                else:
                    addition = l1.val + l2.val
                    iterator.next = ListNode(addition % 10)
                    iterator = iterator.next
                    checker = int(floor(addition / 10))
                    print(checker,'ghjk')
                    if checker:
                        extra = checker
                    else:
                        extra = 0
                l1 = l1.next
                l2 = l2.next
            elif l1:

                if extra:
                    addition = l1.val + extra
                    if addition >= 10:
                        iterator.next = ListNode(addition % 10)
                        iterator = iterator.next
                        checker = int(floor(addition / 10))
                        print(checker)
                        if checker:
                            extra = checker
                        else:
                            extra = 0
                    else:
                        iterator.next = ListNode(addition % 10)
                        iterator = iterator.next
                        print(int(floor(addition / 10)))
                        checker = int(floor(addition / 10))
                        if checker:
                            extra = checker
                        else:
                            extra = 0
                else:
                        addition = l1.val 
                        print(addition,'dfghjhgfd')
                        iterator.next = ListNode(addition % 10)
                        iterator = iterator.next
                        checker = int(floor(addition / 10))
                        if checker:
                            extra = checker
                        else:
                            extra = 0

                l1 = l1.next
            elif l2:
                if extra:
                    addition = l2.val + extra
                    if addition >= 10:
                        iterator.next = ListNode(addition % 10)
                        iterator = iterator.next
                        checker = int(floor(addition / 10))
                        if checker:
                            extra = checker
                        else:
                            extra = 0
                    else:
                        iterator.next = ListNode(addition % 10)
                        iterator = iterator.next
                        print(int(floor(addition / 10)))
                        checker = int(floor(addition / 10))
                        if checker:
                            extra = checker
                        else:
                            extra = 0
                else:
                        addition = l2.val 
                        iterator.next = ListNode(addition % 10)
                        iterator = iterator.next
                        checker = int(floor(addition / 10))
                        if checker:
                            extra = checker
                        else:
                            extra = 0
                    
                l2 = l2.next
        if extra:
            iterator.next = ListNode(extra)

        return result.next