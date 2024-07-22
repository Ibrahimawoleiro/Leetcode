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
    func preorderTraversal(_ root: TreeNode?) -> [Int] {
        func preorder(root curr: TreeNode?, array arr: inout [Int]) -> [Int]{
            guard let curr = curr else {return []}

            
            arr.append(curr.val)
            preorder(root : curr.left, array: &arr)
            preorder(root: curr.right,array: &arr)
            return arr
        }
        var ans: [Int] = [Int]()

        return preorder(root: root, array: &ans)
    }
    
}