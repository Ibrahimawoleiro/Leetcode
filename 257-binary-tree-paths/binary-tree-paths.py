# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        self.helper(root, result, [])
        return result


    def helper(self, root, result, current_path):
        if not root.left and not root.right:
            current_path.append(str(root.val))
            result.append('->'.join(current_path))
        print(current_path, root.val)
        if root.left:
            self.helper(root.left, result, current_path.copy()+[str(root.val)])
        if root.right:
            self.helper(root.right, result, current_path.copy()+[str(root.val)])