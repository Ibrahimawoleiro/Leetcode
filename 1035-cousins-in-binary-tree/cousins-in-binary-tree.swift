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
    func isCousins(_ root: TreeNode?, _ x: Int, _ y: Int) -> Bool {
        //store -> (depth, parent, parent seen)
        var store: [Int: (Int, Int, Bool)] = [Int: (Int, Int, Bool)]();
        //depth_counter
        var d_c: Int = 0;
        self.traversal(root, d_c, &store, x, y);
        if let x_value = store[x],let y_value = store[y]{
            print(x_value, y_value)
            return x_value.0 == y_value.0 && x_value.1 != y_value.1;
        }
        return false;
    }

    func traversal(_ root: TreeNode?, _ d_c: Int, _ store: inout [Int: (Int, Int, Bool)], _ x: Int, _ y: Int) -> Void{
        guard let root = root else { return }
        
        if root.val == x {
            store[x] = (d_c,-1, false);
            return 
        }else if root.val == y{
            store[y] = (d_c,-1, false);
            return 
        }
        if let x_value = store[x]{
            if root.val != x && x_value.2 == false{
                store[x] = (x_value.0, root.val, true)
            }
        }
        if let y_value = store[y]{
            if root.val != y && y_value.2 == false{
                store[y] = (y_value.0, root.val, true)
            }
        }
        self.traversal(root.left, d_c + 1 , &store, x,y);
        self.traversal(root.right, d_c + 1, &store, x, y);
    }
}