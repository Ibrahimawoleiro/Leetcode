"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        r = head
        def copy_maker(node):
            if not node:
                return
            next_ = node.next
            copied = Node(node.val)
            node.next = copied
            copied.next = next_
            copy_maker(node.next.next)

        def random_maker(node):
            if not node: 
                return
            if not node.random:
                node.next.random = node.random
            else:
                node.next.random = node.random.next
            random_maker(node.next.next)

        def separator(node):
            if not node:
                return (None, None)
            original = node
            copied = node.next
            s_p = copied.next
            original.next, copied.next = separator(s_p)
            return original, copied


        
        copy_maker(r)
        random_maker(r)
        return separator(r)[1]

        

