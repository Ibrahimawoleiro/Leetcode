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
    func sumRootToLeaf(_ root: TreeNode?) -> Int {
        var total: Int = 0;
        var ans: [[Int]] = [[Int]]();
        var tracker: [Int] = [Int]();
        self.recursive(root, &ans, &tracker);
        print(ans.count)
        for arr in ans{
            var curr: Int = 0;
            print(arr)
            var runner: Int = arr.count - 1;
            var power: Int = 0;
            while(runner >= 0){
                curr += arr[runner] * Int(pow(2.0, Double(power)));
                power+=1;
                runner -= 1;
            }
            total += curr;
        }
        return total;
    }

    func recursive(_ root: TreeNode?, _ arr: inout [[Int]], _ tracker: inout [Int]) -> Void{
        guard let root = root else { 
            return;
         };
         tracker.append(root.val);

         if root.right == nil && root.left == nil{
            print("tracker \(tracker)");
            arr.append(Array(tracker)); 
         }else if root.right != nil && root.left == nil{
            self.recursive(root.right, &arr, &tracker);
         }else if root.left != nil && root.right == nil{
            self.recursive(root.left, &arr, &tracker);
         }else{
            self.recursive(root.left, &arr, &tracker);
            self.recursive(root.right, &arr, &tracker);
         }
        tracker.removeLast()
    }
}