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
        var result : [Int] = [Int]();
        self.recursive(root: root, &result);
        return result;
    }

    func recursive(root curr: TreeNode?, _ ans: inout [Int]) -> Void{
        guard let curr = curr else {return }
        print("u");
        self.recursive(root: curr.left, &ans)
        ans.append(curr.val);
        self.recursive(root: curr.right, &ans)
    }
}