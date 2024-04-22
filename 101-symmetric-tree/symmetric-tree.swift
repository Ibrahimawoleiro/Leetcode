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
    func isSymmetric(_ root: TreeNode?) -> Bool {
        
        return self.recursive(left_child: root!.left, right_child: root!.right);
    }

    func recursive(left_child left: TreeNode?, right_child right: TreeNode?) -> Bool{
        if(left == nil && right == nil){
            return true;
        }else if(left == nil || right == nil){
            return false;
        }
        if let left = left, let right = right{
            if left.val == right.val{
                return self.recursive(left_child : left.left, right_child : right.right) && self.recursive(left_child : left.right, right_child : right.left)
            }else{
                return false;
            }
        }
        return false;
    }
}