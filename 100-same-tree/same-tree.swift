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
    func isSameTree(_ p: TreeNode?, _ q: TreeNode?) -> Bool {
        
        guard let p = p, let q = q else {
            if let p = p{
                return false;
            }
            if let q = q {
                return false;
            }
            return true;
        }

        if p.val != q.val{
            return false;
        }

        return self.isSameTree(p.left, q.left) && self.isSameTree(p.right, q.right);
    }
}