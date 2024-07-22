/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init() { self.val = 0; self.left = nil; self.right = nil; }
 *     public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
 *     public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
 *         self.val = val
 *         self.left = left
 *         self.right = right
 *     }
 * }
 */
class Solution {
    func isBalanced(_ root: TreeNode?) -> Bool {
        func balanced(current node: TreeNode?) -> (Int, Bool){
            guard let curr = node else {return (0, true)};
            var left: (Int, Bool) = balanced(current: curr.left);
            if !left.1{
                return (0, false);
            }
            var right: (Int, Bool) = balanced(current: curr.right);
            if !right.1{
                return (0, false);
            }

            if abs(left.0 - right.0) > 1{
                return (0, false);
            }

            return (max(left.0, right.0) + 1, true)
        }

        return balanced(current: root).1;
    }
}