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
    func sumOfLeftLeaves(_ root: TreeNode?) -> Int {
        var sum = 0
        traverse(root, direction: nil, sum: &sum)
        return sum
    }

    private func traverse(_ node: TreeNode?, direction: Character?, sum: inout Int) {
        guard let node = node else { return }

        if node.left == nil && node.right == nil && direction == "l" {
            sum += node.val
        }

        traverse(node.left, direction: "l", sum: &sum)
        traverse(node.right, direction: "r", sum: &sum)
    }
}