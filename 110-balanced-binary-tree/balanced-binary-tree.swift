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
        return self.recursive(root).1;
    }

    func recursive(_ root: TreeNode?) -> (Int, Bool){
        guard let root = root else {return (0, true)};
        var left_result : (Int, Bool) = self.recursive(root.left);
        if left_result.1 == false{
            return (0, false)
        }
        var right_result : (Int, Bool) = self.recursive(root.right);
        if right_result.1 == false{
            return (0, false)
        }
        return ( max(left_result.0 + 1, right_result.0 + 1), abs(left_result.0 - right_result.0) <= 1 );
    }
}