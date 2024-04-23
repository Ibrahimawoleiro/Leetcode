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
        return self.recursive(p, q);
    }

    func recursive(_ left: TreeNode?, _ right: TreeNode?) -> Bool{
        if let left = left , let right = right{

            if left.val != right.val{
                return false
            }
            return self.recursive(left.left, right.left) && self.recursive(left.right, right.right);
        }else if let left = left{
            return false;
        }else if let right = right{
            return false;
        }
        else{
            return true;
        }
    }
}