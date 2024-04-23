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
    func findTilt(_ root: TreeNode?) -> Int {
        return recursive(root).1;
    }

    func recursive(_ root: TreeNode?) -> (Int, Int){
        guard let root = root else {return (0,0)};

        var left: (Int, Int) = recursive(root.left);

        var right: (Int, Int) = recursive(root.right);

        var sum_till_now :Int = left.0 + right.0 + root.val;

        var tilt_till_now : Int = left.1 + right.1 + abs(left.0 - right.0);

        return (sum_till_now, tilt_till_now);
    }
}