# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        left_holder = None
        right_holder =None
        position_count = 1
        if left == right:
            return head
        
        if left == 1:
            left_holder = head
            current = head
            previous = None
            next_node = current.next
            
            while position_count <= right:
                if position_count == right:
                    head = current
                current.next = previous
                previous = current
                current = next_node
                if(next_node!=None):
                    next_node = current.next
                position_count+=1
            
            left_holder.next = current
            
        if left > 1:
            current = head
            previous = None
            next_node = None
            position_count = 1
            left_node = None
            
            while(position_count <= right):
                if position_count == left - 1:
                    left_holder = current
                if(position_count >= left):
                    if(position_count == right):
                        current.next = previous
                        previous = current
                        current = next_node
                        break
                    if position_count == left:
                        left_node = current
                        next_node = current.next
                    current.next = previous
                    previous = current
                    current = next_node
                    next_node = current.next
                    position_count+=1
                    continue
                current = current.next
                position_count+=1
            left_holder.next = previous
            left_node.next = current
        return head
            
                
                
            