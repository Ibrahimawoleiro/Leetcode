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
    func rangeSumBST(_ root: TreeNode?, _ low: Int, _ high: Int) -> Int {
        var sum: Int = 0;
        self.r(root, low, high, &sum);
        return sum;
    }
    
    func r(_ root: TreeNode?, _ low : Int, _ high : Int, _ sum: inout Int) -> Void{
        guard let root = root else {return };
        if root.val >= low && root.val <= high{
            sum += root.val;
        }
        self.r(root.left, low, high, &sum)
        self.r(root.right, low, high, &sum)

    }
}