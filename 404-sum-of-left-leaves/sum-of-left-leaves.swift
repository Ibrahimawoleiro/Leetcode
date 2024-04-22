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
        var sum: Int = 0;
        self.recursive(root, &sum, direction:" ");
        return sum
    }

    func recursive(_ root: TreeNode?, _ sum: inout Int, direction d: Character) -> Void {
        guard let root = root else {return }
        if let left = root.left, let right = root.right{

        }else if let left = root.left{

        }
        else if let right = root.right{

        }else{
            if d == "l"{
                sum += root.val
            }
        }
        self.recursive(root.left, &sum, direction: "l");
        self.recursive(root.right, &sum, direction: "r");
    }
}