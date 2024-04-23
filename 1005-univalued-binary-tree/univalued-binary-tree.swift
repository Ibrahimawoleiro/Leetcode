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
    func isUnivalTree(_ root: TreeNode?) -> Bool {
        return recursive(root, root!.val);
    }
    func recursive(_ root: TreeNode?, _ a: Int)-> Bool{
        guard let root = root else {return true};
        if root.val != a{
            return false;
        }
        return recursive(root.left, a) && recursive(root.right, a);
    }
}