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
    func inorderTraversal(_ root: TreeNode?) -> [Int] {
        func inorder(root curr: TreeNode?, array arr: inout [Int]) -> [Int]{
            guard let curr = curr else {return []}

            inorder(root : curr.left, array: &arr)
            arr.append(curr.val)
            inorder(root: curr.right,array: &arr)
            return arr
        }
        var ans: [Int] = [Int]()

        return inorder(root: root, array: &ans)
    }
}