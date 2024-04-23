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
    func getMinimumDifference(_ root: TreeNode?) -> Int {
        var ans: [Int] = [Int](); 
        var minimum: Int = 10 * 10 * 10 * 10 * 10 * 10 
        self.recursive(root, &ans);
        var i : Int = 0;
        var j : Int = 0;
        while(j < ans.count){
            if i == j{
                j+=1;
                continue;
            }
            var curr_difference: Int = ans[j] - ans[i];
            if curr_difference < minimum{
                minimum = curr_difference;
                j+=1;
            }else{
                i+=1;
            }
        }
        return minimum;
    }

    func recursive(_ root: TreeNode?, _ ans: inout [Int]) -> Void{
        guard let root = root else {return };
        self.recursive(root.left, &ans);
        ans.append(root.val)
        self.recursive(root.right, &ans);
    }
}