# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        node = root
        while(node):
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        curr = self.stack[-1].val
        print(curr)
        node = self.stack.pop()
        if node.right:
            node = node.right
            while(node):
                self.stack.append(node)
                node = node.left
        return curr
    def hasNext(self) -> bool:
        return len(self.stack) > 0




# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()