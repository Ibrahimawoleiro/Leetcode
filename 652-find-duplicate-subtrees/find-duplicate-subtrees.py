# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        store = set()
        checker = {}
        def helper(curr,checker, store,combo):
            if not curr:
                return 'null,'

            left_combo = helper(curr.left,checker, store, '')

            

            combo += f'{curr.val},'
            combo += left_combo
            right_combo = helper(curr.right,checker, store, '')

            combo += right_combo

            print(combo)
            if combo in checker and not checker[combo]:
                store.add(curr)
                checker[combo] = True
            elif combo not in checker:
                checker[combo] = False
            
            return combo

        helper(root, checker, store, '')
        return list(store)

            


            
            