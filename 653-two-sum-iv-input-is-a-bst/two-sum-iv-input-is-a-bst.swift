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
    func findTarget(_ root: TreeNode?, _ k: Int) -> Bool {
        var store: Set<Int> = Set<Int>();
        var ans: Bool? = self.recursive(root, &store, k);
        if let ans{
            return true;
        }
        return false;
    }
    func recursive(_ root: TreeNode?, _ store: inout Set<Int>, _ k: Int) -> Bool?{
        guard let root = root else{return nil};

        if store.contains(k - root.val ){
            return true;
        }

        store.insert(root.val);

        if let l = self.recursive(root.left, &store, k){
            return true;
        }else if let r = self.recursive(root.right, &store, k){
            return true;
        }
        return nil;
    }
}