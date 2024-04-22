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
    func mergeTrees(_ root1: TreeNode?, _ root2: TreeNode?) -> TreeNode? {
        return self.recursive(left_child : root1, right_child : root2)
    }

    func recursive(left_child root1: TreeNode?, right_child root2: TreeNode?) -> TreeNode?{
        if let left: TreeNode = root1, let right: TreeNode = root2{
            let curr_value = left.val + right.val;
            print(curr_value)
            var left_child: TreeNode? = self.recursive(left_child : left.left, right_child : right.left);
            var right_child: TreeNode? = self.recursive(left_child : left.right, right_child : right.right);
            var curr_node: TreeNode? = TreeNode(curr_value);
            if let left_child = left_child{
                curr_node?.left = left_child;
            }else{
                curr_node?.left = nil;
            }
            if let right_child = right_child{
                curr_node?.right = right_child;
            }else{
                curr_node?.right = nil;
            }
            
            return curr_node;





        }else if let left: TreeNode = root1{
            let curr_value = left.val;
            print(curr_value)
            var left_child: TreeNode? = self.recursive(left_child : left.left, right_child : nil);
            var right_child: TreeNode? = self.recursive(left_child : left.right, right_child : nil);
            var curr_node: TreeNode? = TreeNode(curr_value)
            if let left_child = left_child{
                curr_node?.left = left_child;
            }else{
                curr_node?.left = nil;
            }
            if let right_child = right_child{
                curr_node?.right = right_child;
            }else{
                curr_node?.right = nil;
            }
            return curr_node;




        }else if let right: TreeNode = root2{
            let curr_value = right.val;
            print(curr_value)
            var left_child: TreeNode? = self.recursive(left_child : nil, right_child : right.left);
            var right_child: TreeNode? = self.recursive(left_child : nil, right_child : right.right);
            var curr_node: TreeNode? = TreeNode(curr_value)
            if let left_child = left_child{
                curr_node?.left = left_child;
            }else{
                curr_node?.left = nil;
            }
            if let right_child = right_child{
                curr_node?.right = right_child;
            }else{
                curr_node?.right = nil;
            }
            return curr_node;
        }else{
            return nil
        }
    }
}