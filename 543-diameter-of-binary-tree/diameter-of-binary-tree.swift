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
    func diameterOfBinaryTree(_ root: TreeNode?) -> Int {
        return  self.recursive(child: root)[1];
    }

    func recursive(child root: TreeNode?)-> [Int]{
        guard let root = root else { return [-1,-1]};

        var left: [Int] = self.recursive(child: root.left);
        left[0] += 1;
        var right: [Int] = self.recursive(child: root.right);
        right[0] += 1;
        var longest_to_leaf: Int = max(left[0], right[0]);
        var max_in_one_side: Int = max(right[1], left[1]);
        var max_in_left_plus_right: Int = right[0] + left[0]
        return [longest_to_leaf, max(max_in_left_plus_right, max_in_one_side)]
    }
}