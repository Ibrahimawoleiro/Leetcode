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
    func leafSimilar(_ root1: TreeNode?, _ root2: TreeNode?) -> Bool {
        var queue: [Int] = [Int]()
        self.traversal1(root1, &queue);
        print(queue)
        return self.traversal2(root2, &queue) && queue.count == 0;
    }
    func traversal1(_ root: TreeNode?, _ queue: inout [Int]) -> Void{
        guard let root = root else {return}
        self.traversal1(root.left, &queue);
        if root.left == nil && root.right == nil{
            queue.append(root.val)
        }
        self.traversal1(root.right, &queue);
    }

    func traversal2(_ root: TreeNode?, _ queue: inout [Int]) -> Bool{
        guard let root = root else {return true}
        if root.left == nil && root.right == nil{
            if queue.count == 0{
                return false;
            }
            var enqueue : Int = queue.removeFirst()
            if root.val != enqueue {
                print(root.val, enqueue)
                return false;
            }
        }
        return self.traversal2(root.left, &queue) && self.traversal2(root.right, &queue);
    }
}