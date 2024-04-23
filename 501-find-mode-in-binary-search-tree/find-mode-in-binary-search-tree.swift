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
    func findMode(_ root: TreeNode?) -> [Int] {
        var store: [Int: Int] = [Int: Int]();
        var maximum: Int = 1;
        self.recursive(root, &store, &maximum)
        var ans: [Int] = [Int]()
        for key in store.keys{
            if let curr = store[key]{
                if curr == maximum{
                    ans.append(key)
                }
            }
        }
        return ans;
    }
    func recursive(_ root: TreeNode?, _ store: inout [Int: Int], _ m: inout Int) -> Void{
        
        guard let root = root else { return };
        self.recursive(root.left, &store, &m)
        if let curr = store[root.val]{
            var current =  curr + 1
            store[root.val] = current;
            if m < current{
                m = current
            }
        }else{
            store[root.val] =  1;
        }
        self.recursive(root.right, &store, &m)

        
    }
}