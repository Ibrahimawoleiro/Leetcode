# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        main_queue = deque()
        main_array = []
        children_queue = deque()
        inner_array = []
        main_queue.append(root)
        while(main_queue):
            curr =  main_queue.popleft()
            if curr.left:
                children_queue.append(curr.left)
            if curr.right:
                children_queue.append(curr.right)
            inner_array.append(curr.val)
            if len(main_queue) == 0:
               main_queue = children_queue
               children_queue = deque()
               main_array.append(inner_array)
               inner_array = []

        return main_array
        